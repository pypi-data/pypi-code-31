import itertools
from datetime import datetime

from raiden.messages import Lock
from raiden.storage.serialize import JSONSerializer
from raiden.storage.sqlite import SQLiteStorage
from raiden.tests.utils import factories
from raiden.transfer.events import SendDirectTransfer
from raiden.transfer.mediated_transfer.events import (
    SendBalanceProof,
    SendLockedTransfer,
    SendLockExpired,
    SendRefundTransfer,
)
from raiden.transfer.mediated_transfer.state_change import (
    ActionInitMediator,
    ActionInitTarget,
    ReceiveLockExpired,
    ReceiveTransferRefund,
    ReceiveTransferRefundCancelRoute,
)
from raiden.transfer.state import BalanceProofUnsignedState
from raiden.transfer.state_change import ReceiveTransferDirect, ReceiveUnlock
from raiden.transfer.utils import get_event_with_balance_proof, get_state_change_with_balance_proof
from raiden.utils import sha3


def make_signed_balance_proof_from_counter(counter):
    lock = Lock(
        amount=next(counter),
        expiration=next(counter),
        secrethash=sha3(factories.make_secret(next(counter))),
    )
    lock_expired_balance_proof = factories.make_signed_balance_proof(
        nonce=next(counter),
        transferred_amount=next(counter),
        locked_amount=next(counter),
        token_network_address=factories.make_address(),
        channel_identifier=next(counter),
        locksroot=sha3(lock.as_bytes),
        extra_hash=sha3(b''),
        private_key=factories.HOP1_KEY,
        sender_address=factories.HOP1,
    )

    return lock_expired_balance_proof


def make_balance_proof_from_counter(counter) -> BalanceProofUnsignedState:
    return BalanceProofUnsignedState(
        nonce=next(counter),
        transferred_amount=next(counter),
        locked_amount=next(counter),
        locksroot=sha3(next(counter).to_bytes(1, 'big')),
        token_network_identifier=factories.make_address(),
        channel_identifier=next(counter),
        chain_id=next(counter),
    )


def make_transfer_from_counter(counter):
    return factories.make_transfer(
        amount=next(counter),
        initiator=factories.make_address(),
        target=factories.make_address(),
        expiration=next(counter),
        secret=factories.make_secret(next(counter)),
    )


def make_signed_transfer_from_counter(counter):
    lock = Lock(
        amount=next(counter),
        expiration=next(counter),
        secrethash=sha3(factories.make_secret(next(counter))),
    )

    signed_transfer = factories.make_signed_transfer(
        amount=next(counter),
        initiator=factories.make_address(),
        target=factories.make_address(),
        expiration=next(counter),
        secret=factories.make_secret(next(counter)),
        payment_identifier=next(counter),
        message_identifier=next(counter),
        nonce=next(counter),
        transferred_amount=next(counter),
        locked_amount=next(counter),
        locksroot=sha3(lock.as_bytes),
        recipient=factories.make_address(),
        channel_identifier=next(counter),
        token_network_address=factories.make_address(),
        token=factories.make_address(),
        pkey=factories.HOP1_KEY,
        sender=factories.HOP1,
    )

    return signed_transfer


def make_from_route_from_counter(counter):
    from_channel = factories.make_channel(
        partner_balance=next(counter),
        partner_address=factories.HOP1,
        token_address=factories.make_address(),
        channel_identifier=next(counter),
    )
    from_route = factories.route_from_channel(from_channel)

    expiration = factories.UNIT_REVEAL_TIMEOUT + 1

    from_transfer = factories.make_signed_transfer_for(
        channel_state=from_channel,
        amount=1,
        initiator=factories.make_address(),
        target=factories.make_address(),
        expiration=expiration,
        secret=sha3(factories.make_secret(next(counter))),
        identifier=next(counter),
        nonce=1,
        transferred_amount=0,
        pkey=factories.HOP1_KEY,
        sender=factories.HOP1,
    )
    return from_route, from_transfer


def test_get_state_change_with_balance_proof():
    """ All state changes which contain a balance proof must be found by when
    querying the database.
    """
    serializer = JSONSerializer
    storage = SQLiteStorage(':memory:', serializer)
    counter = itertools.count()

    lock_expired = ReceiveLockExpired(
        balance_proof=make_signed_balance_proof_from_counter(counter),
        secrethash=sha3(factories.make_secret(next(counter))),
        message_identifier=next(counter),
    )
    transfer_direct = ReceiveTransferDirect(
        token_network_identifier=factories.make_address(),
        message_identifier=next(counter),
        payment_identifier=next(counter),
        balance_proof=make_signed_balance_proof_from_counter(counter),
    )
    unlock = ReceiveUnlock(
        message_identifier=next(counter),
        secret=sha3(factories.make_secret(next(counter))),
        balance_proof=make_signed_balance_proof_from_counter(counter),
    )
    transfer_refund = ReceiveTransferRefund(
        transfer=make_signed_transfer_from_counter(counter),
        routes=list(),
    )
    transfer_refund_cancel_route = ReceiveTransferRefundCancelRoute(
        routes=list(),
        transfer=make_signed_transfer_from_counter(counter),
        secret=sha3(factories.make_secret(next(counter))),
    )
    mediator_from_route, mediator_signed_transfer = make_from_route_from_counter(counter)
    action_init_mediator = ActionInitMediator(
        routes=list(),
        from_route=mediator_from_route,
        from_transfer=mediator_signed_transfer,
    )
    target_from_route, target_signed_transfer = make_from_route_from_counter(counter)
    action_init_target = ActionInitTarget(
        route=target_from_route,
        transfer=target_signed_transfer,
    )

    statechanges_balanceproofs = [
        (lock_expired, lock_expired.balance_proof),
        (transfer_direct, transfer_direct.balance_proof),
        (unlock, unlock.balance_proof),
        (transfer_refund, transfer_refund.transfer.balance_proof),
        (transfer_refund_cancel_route, transfer_refund_cancel_route.transfer.balance_proof),
        (action_init_mediator, action_init_mediator.from_transfer.balance_proof),
        (action_init_target, action_init_target.transfer.balance_proof),
    ]

    timestamp = datetime.utcnow().isoformat(timespec='milliseconds')

    for state_change, _ in statechanges_balanceproofs:
        storage.write_state_change(state_change, timestamp)

    for state_change, balance_proof in statechanges_balanceproofs:
        state_change_record = get_state_change_with_balance_proof(
            storage=storage,
            chain_id=balance_proof.chain_id,
            token_network_identifier=balance_proof.token_network_identifier,
            channel_identifier=balance_proof.channel_identifier,
            sender=balance_proof.sender,
            balance_hash=balance_proof.balance_hash,
        )
        assert state_change_record.data == state_change


def test_get_event_with_balance_proof():
    """ All events which contain a balance proof must be found by when
    querying the database.
    """
    serializer = JSONSerializer
    storage = SQLiteStorage(':memory:', serializer)
    counter = itertools.count()

    direct_transfer = SendDirectTransfer(
        recipient=factories.make_address(),
        channel_identifier=next(counter),
        message_identifier=next(counter),
        payment_identifier=next(counter),
        balance_proof=make_balance_proof_from_counter(counter),
        token_address=factories.make_address(),
    )
    lock_expired = SendLockExpired(
        recipient=factories.make_address(),
        message_identifier=next(counter),
        balance_proof=make_balance_proof_from_counter(counter),
        secrethash=sha3(factories.make_secret(next(counter))),
    )
    locked_transfer = SendLockedTransfer(
        recipient=factories.make_address(),
        channel_identifier=factories.make_channel_identifier(),
        message_identifier=next(counter),
        transfer=make_transfer_from_counter(counter),
    )
    balance_proof = SendBalanceProof(
        recipient=factories.make_address(),
        channel_identifier=factories.make_channel_identifier(),
        message_identifier=next(counter),
        payment_identifier=next(counter),
        token_address=factories.make_address(),
        secret=factories.make_secret(next(counter)),
        balance_proof=make_balance_proof_from_counter(counter),
    )
    refund_transfer = SendRefundTransfer(
        recipient=factories.make_address(),
        channel_identifier=factories.make_channel_identifier(),
        message_identifier=next(counter),
        transfer=make_transfer_from_counter(counter),
    )

    events_balanceproofs = [
        (direct_transfer, direct_transfer.balance_proof),
        (lock_expired, lock_expired.balance_proof),
        (locked_transfer, locked_transfer.balance_proof),
        (balance_proof, balance_proof.balance_proof),
        (refund_transfer, refund_transfer.transfer.balance_proof),
    ]

    timestamp = datetime.utcnow().isoformat(timespec='milliseconds')
    state_change = ''
    for event, _ in events_balanceproofs:
        state_change_identifier = storage.write_state_change(
            state_change,
            timestamp,
        )
        storage.write_events(
            state_change_identifier=state_change_identifier,
            events=[event],
            log_time=timestamp,
        )

    for event, balance_proof in events_balanceproofs:
        event_record = get_event_with_balance_proof(
            storage=storage,
            chain_id=balance_proof.chain_id,
            token_network_identifier=balance_proof.token_network_identifier,
            channel_identifier=balance_proof.channel_identifier,
            balance_hash=balance_proof.balance_hash,
        )
        assert event_record.data == event
