from typing import Any, Dict, Generator, List, Tuple

import cytoolz
from eth_utils import is_same_address, to_bytes, to_tuple
from web3 import Web3

from ethpm.exceptions import BytecodeLinkingError, ValidationError


def get_linked_deployments(deployments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Returns all deployments found in a chain URI's deployment data that contain link dependencies.
    """
    linked_deployments = {
        dep: data
        for dep, data in deployments.items()
        if cytoolz.get_in(("runtime_bytecode", "link_dependencies"), data)
    }
    for deployment, data in linked_deployments.items():
        if any(
            link_dep["value"] == deployment
            for link_dep in data["runtime_bytecode"]["link_dependencies"]
        ):
            raise BytecodeLinkingError(
                f"Link dependency found in {deployment} deployment that references its "
                "own contract instance, which is disallowed"
            )
    return linked_deployments


def validate_linked_references(
    link_deps: Tuple[Tuple[int, str]], bytecode: bytes
) -> None:
    """
    Validates that normalized linked_references (offset, expected_bytes)
    match the corresponding bytecode.
    """
    offsets, values = zip(*link_deps)
    for idx, offset in enumerate(offsets):
        value = values[idx]
        # https://github.com/python/mypy/issues/4975
        offset_value = int(offset)  # type: ignore
        dep_length = len(value)  # type: ignore
        end_of_bytes = offset_value + dep_length
        # Ignore b/c whitespace around ':' conflict b/w black & flake8
        actual_bytes = bytecode[offset_value:end_of_bytes]  # noqa: E203
        if actual_bytes != values[idx]:
            raise ValidationError(
                "Error validating linked reference. "
                f"Offset: {offset} "
                f"Value: {values[idx]} "
                f"Bytecode: {bytecode} ."
            )


@to_tuple
def normalize_linked_references(
    data: List[Dict[str, Any]]
) -> Generator[Tuple[int, str, str], None, None]:
    """
    Return a tuple of information representing all insertions of a linked reference.
    (offset, type, value)
    """
    for deployment in data:
        for offset in deployment["offsets"]:
            yield offset, deployment["type"], deployment["value"]


def validate_deployments_tx_receipt(
    deployments: Dict[str, Any], w3: Web3, allow_missing_data: bool = False
) -> None:
    """
    Validate that address and block hash found in deployment data match what is found on-chain.
    """
    # todo: provide hook to lazily look up tx receipt via binary search if missing data
    for name, data in deployments.items():
        if "transaction" in data:
            tx_hash = data["transaction"]
            tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
            tx_address = tx_receipt["contractAddress"]

            # case when on-chain factory used to deploy a contract
            if "contractAddress" not in tx_receipt and allow_missing_data is False:
                raise ValidationError(
                    "No contract address found in tx receipt. "
                    "Unable to verify address in deployment data. "
                    "If this validation is not necessary, please enable `allow_missing_data` arg."
                )

            if not is_same_address(tx_address, data["address"]):
                raise ValidationError(
                    f"Error validating tx_receipt for {name} deployment. "
                    f"Address found in deployment: {data['address']} "
                    "Does not match "
                    f"Address found on tx_receipt: {tx_address}."
                )

            if "block" in data:
                if tx_receipt["blockHash"] != to_bytes(hexstr=data["block"]):
                    raise ValidationError(
                        f"Error validating tx_receipt for {name} deployment. "
                        f"Block found in deployment: {data['block']} "
                        "Does not match "
                        f"Block found on tx_receipt: {tx_receipt['blockHash']}."
                    )
            elif allow_missing_data is False:
                raise ValidationError(
                    "No block hash found in deployment data. "
                    "Unable to verify block hash on tx receipt. "
                    "If this validation is not necessary, please enable `allow_missing_data` arg."
                )
        elif allow_missing_data is False:
            raise ValidationError(
                "No transaction hash found in deployment data. "
                "Unable to validate tx_receipt. "
                "If this validation is not necessary, please enable `allow_missing_data` arg."
            )
