# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

import json
from twilio.twiml import (
    TwiML,
    format_language,
)


class VoiceResponse(TwiML):
    """ <Response> TwiML for Voice """

    def __init__(self, **kwargs):
        super(VoiceResponse, self).__init__(**kwargs)
        self.name = 'Response'

    def connect(self, action=None, method=None, **kwargs):
        """
        Create a <Connect> element

        :param action: Action URL
        :param method: Action URL method
        :param kwargs: additional attributes

        :returns: <Connect> element
        """
        return self.nest(Connect(action=action, method=method, **kwargs))

    def dial(self, number=None, action=None, method=None, timeout=None,
             hangup_on_star=None, time_limit=None, caller_id=None, record=None,
             trim=None, recording_status_callback=None,
             recording_status_callback_method=None,
             recording_status_callback_event=None, answer_on_bridge=None,
             ring_tone=None, **kwargs):
        """
        Create a <Dial> element

        :param number: Phone number to dial
        :param action: Action URL
        :param method: Action URL method
        :param timeout: Time to wait for answer
        :param hangup_on_star: Hangup call on star press
        :param time_limit: Max time length
        :param caller_id: Caller ID to display
        :param record: Record the call
        :param trim: Trim the recording
        :param recording_status_callback: Recording status callback URL
        :param recording_status_callback_method: Recording status callback URL method
        :param recording_status_callback_event: Recording status callback events
        :param answer_on_bridge: Preserve the ringing behavior of the inbound call until the Dialed call picks up
        :param ring_tone: Ringtone allows you to override the ringback tone that Twilio will play back to the caller while executing the Dial
        :param kwargs: additional attributes

        :returns: <Dial> element
        """
        return self.nest(Dial(
            number=number,
            action=action,
            method=method,
            timeout=timeout,
            hangup_on_star=hangup_on_star,
            time_limit=time_limit,
            caller_id=caller_id,
            record=record,
            trim=trim,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            recording_status_callback_event=recording_status_callback_event,
            answer_on_bridge=answer_on_bridge,
            ring_tone=ring_tone,
            **kwargs
        ))

    def echo(self, **kwargs):
        """
        Create a <Echo> element

        :param kwargs: additional attributes

        :returns: <Echo> element
        """
        return self.nest(Echo(**kwargs))

    def enqueue(self, name=None, action=None, method=None, wait_url=None,
                wait_url_method=None, workflow_sid=None, **kwargs):
        """
        Create a <Enqueue> element

        :param name: Friendly name
        :param action: Action URL
        :param method: Action URL method
        :param wait_url: Wait URL
        :param wait_url_method: Wait URL method
        :param workflow_sid: TaskRouter Workflow SID
        :param kwargs: additional attributes

        :returns: <Enqueue> element
        """
        return self.nest(Enqueue(
            name=name,
            action=action,
            method=method,
            wait_url=wait_url,
            wait_url_method=wait_url_method,
            workflow_sid=workflow_sid,
            **kwargs
        ))

    def gather(self, input=None, action=None, method=None, timeout=None,
               speech_timeout=None, max_speech_time=None, profanity_filter=None,
               finish_on_key=None, num_digits=None, partial_result_callback=None,
               partial_result_callback_method=None, language=None, hints=None,
               barge_in=None, debug=None, **kwargs):
        """
        Create a <Gather> element

        :param input: Input type Twilio should accept
        :param action: Action URL
        :param method: Action URL method
        :param timeout: Time to wait to gather input
        :param speech_timeout: Time to wait to gather speech input and it should be either auto or a positive integer.
        :param max_speech_time: Max allowed time for speech input
        :param profanity_filter: Profanity Filter on speech
        :param finish_on_key: Finish gather on key
        :param num_digits: Number of digits to collect
        :param partial_result_callback: Partial result callback URL
        :param partial_result_callback_method: Partial result callback URL method
        :param language: Language to use
        :param hints: Speech recognition hints
        :param barge_in: Stop playing media upon speech
        :param debug: Allow debug for gather
        :param kwargs: additional attributes

        :returns: <Gather> element
        """
        return self.nest(Gather(
            input=input,
            action=action,
            method=method,
            timeout=timeout,
            speech_timeout=speech_timeout,
            max_speech_time=max_speech_time,
            profanity_filter=profanity_filter,
            finish_on_key=finish_on_key,
            num_digits=num_digits,
            partial_result_callback=partial_result_callback,
            partial_result_callback_method=partial_result_callback_method,
            language=language,
            hints=hints,
            barge_in=barge_in,
            debug=debug,
            **kwargs
        ))

    def hangup(self, **kwargs):
        """
        Create a <Hangup> element

        :param kwargs: additional attributes

        :returns: <Hangup> element
        """
        return self.nest(Hangup(**kwargs))

    def leave(self, **kwargs):
        """
        Create a <Leave> element

        :param kwargs: additional attributes

        :returns: <Leave> element
        """
        return self.nest(Leave(**kwargs))

    def pause(self, length=None, **kwargs):
        """
        Create a <Pause> element

        :param length: Length in seconds to pause
        :param kwargs: additional attributes

        :returns: <Pause> element
        """
        return self.nest(Pause(length=length, **kwargs))

    def play(self, url=None, loop=None, digits=None, **kwargs):
        """
        Create a <Play> element

        :param url: Media URL
        :param loop: Times to loop media
        :param digits: Play DTMF tones for digits
        :param kwargs: additional attributes

        :returns: <Play> element
        """
        return self.nest(Play(url=url, loop=loop, digits=digits, **kwargs))

    def queue(self, name, url=None, method=None, reservation_sid=None,
              post_work_activity_sid=None, **kwargs):
        """
        Create a <Queue> element

        :param name: Queue name
        :param url: Action URL
        :param method: Action URL method
        :param reservation_sid: TaskRouter Reservation SID
        :param post_work_activity_sid: TaskRouter Activity SID
        :param kwargs: additional attributes

        :returns: <Queue> element
        """
        return self.nest(Queue(
            name,
            url=url,
            method=method,
            reservation_sid=reservation_sid,
            post_work_activity_sid=post_work_activity_sid,
            **kwargs
        ))

    def record(self, action=None, method=None, timeout=None, finish_on_key=None,
               max_length=None, play_beep=None, trim=None,
               recording_status_callback=None,
               recording_status_callback_method=None, transcribe=None,
               transcribe_callback=None, **kwargs):
        """
        Create a <Record> element

        :param action: Action URL
        :param method: Action URL method
        :param timeout: Timeout to begin recording
        :param finish_on_key: Finish recording on key
        :param max_length: Max time to record in seconds
        :param play_beep: Play beep
        :param trim: Trim the recording
        :param recording_status_callback: Status callback URL
        :param recording_status_callback_method: Status callback URL method
        :param transcribe: Transcribe the recording
        :param transcribe_callback: Transcribe callback URL
        :param kwargs: additional attributes

        :returns: <Record> element
        """
        return self.nest(Record(
            action=action,
            method=method,
            timeout=timeout,
            finish_on_key=finish_on_key,
            max_length=max_length,
            play_beep=play_beep,
            trim=trim,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            transcribe=transcribe,
            transcribe_callback=transcribe_callback,
            **kwargs
        ))

    def redirect(self, url, method=None, **kwargs):
        """
        Create a <Redirect> element

        :param url: Redirect URL
        :param method: Redirect URL method
        :param kwargs: additional attributes

        :returns: <Redirect> element
        """
        return self.nest(Redirect(url, method=method, **kwargs))

    def reject(self, reason=None, **kwargs):
        """
        Create a <Reject> element

        :param reason: Rejection reason
        :param kwargs: additional attributes

        :returns: <Reject> element
        """
        return self.nest(Reject(reason=reason, **kwargs))

    def say(self, message=None, voice=None, loop=None, language=None, **kwargs):
        """
        Create a <Say> element

        :param message: Message to say
        :param voice: Voice to use
        :param loop: Times to loop message
        :param language: Message langauge
        :param kwargs: additional attributes

        :returns: <Say> element
        """
        return self.nest(Say(message=message, voice=voice, loop=loop, language=language, **kwargs))

    def sms(self, message, to=None, from_=None, action=None, method=None,
            status_callback=None, **kwargs):
        """
        Create a <Sms> element

        :param message: Message body
        :param to: Number to send message to
        :param from: Number to send message from
        :param action: Action URL
        :param method: Action URL method
        :param status_callback: Status callback URL
        :param kwargs: additional attributes

        :returns: <Sms> element
        """
        return self.nest(Sms(
            message,
            to=to,
            from_=from_,
            action=action,
            method=method,
            status_callback=status_callback,
            **kwargs
        ))

    def pay(self, input=None, action=None, status_callback=None,
            status_callback_method=None, timeout=None, max_attempts=None,
            security_code=None, postal_code=None, payment_connector=None,
            token_type=None, charge_amount=None, currency=None, description=None,
            valid_card_types=None, language=None, **kwargs):
        """
        Create a <Pay> element

        :param input: Input type Twilio should accept
        :param action: Action URL
        :param status_callback: Status callback URL
        :param status_callback_method: Status callback method
        :param timeout: Time to wait to gather input
        :param max_attempts: Maximum number of allowed retries when gathering input
        :param security_code: Prompt for security code
        :param postal_code: Prompt for postal code and it should be true/false or default postal code
        :param payment_connector: Unique name for payment connector
        :param token_type: Type of token
        :param charge_amount: Amount to process. If value is greater than 0 then make the payment else create a payment token
        :param currency: Currency of the amount attribute
        :param description: Details regarding the payment
        :param valid_card_types: Comma separated accepted card types
        :param language: Language to use
        :param kwargs: additional attributes

        :returns: <Pay> element
        """
        return self.nest(Pay(
            input=input,
            action=action,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            timeout=timeout,
            max_attempts=max_attempts,
            security_code=security_code,
            postal_code=postal_code,
            payment_connector=payment_connector,
            token_type=token_type,
            charge_amount=charge_amount,
            currency=currency,
            description=description,
            valid_card_types=valid_card_types,
            language=language,
            **kwargs
        ))

    def prompt(self, for_=None, error_type=None, card_type=None, attempt=None,
               **kwargs):
        """
        Create a <Prompt> element

        :param for_: Name of the credit card data element
        :param error_type: Type of error
        :param card_type: Type of the credit card
        :param attempt: Current attempt count
        :param kwargs: additional attributes

        :returns: <Prompt> element
        """
        return self.nest(Prompt(
            for_=for_,
            error_type=error_type,
            card_type=card_type,
            attempt=attempt,
            **kwargs
        ))


class Prompt(TwiML):
    """ <Prompt> Twiml Verb """

    def __init__(self, **kwargs):
        super(Prompt, self).__init__(**kwargs)
        self.name = 'Prompt'

    def say(self, message=None, voice=None, loop=None, language=None, **kwargs):
        """
        Create a <Say> element

        :param message: Message to say
        :param voice: Voice to use
        :param loop: Times to loop message
        :param language: Message langauge
        :param kwargs: additional attributes

        :returns: <Say> element
        """
        return self.nest(Say(message=message, voice=voice, loop=loop, language=language, **kwargs))

    def play(self, url=None, loop=None, digits=None, **kwargs):
        """
        Create a <Play> element

        :param url: Media URL
        :param loop: Times to loop media
        :param digits: Play DTMF tones for digits
        :param kwargs: additional attributes

        :returns: <Play> element
        """
        return self.nest(Play(url=url, loop=loop, digits=digits, **kwargs))

    def pause(self, length=None, **kwargs):
        """
        Create a <Pause> element

        :param length: Length in seconds to pause
        :param kwargs: additional attributes

        :returns: <Pause> element
        """
        return self.nest(Pause(length=length, **kwargs))


class Pause(TwiML):
    """ <Pause> TwiML Verb """

    def __init__(self, **kwargs):
        super(Pause, self).__init__(**kwargs)
        self.name = 'Pause'


class Play(TwiML):
    """ <Play> TwiML Verb """

    def __init__(self, url=None, **kwargs):
        super(Play, self).__init__(**kwargs)
        self.name = 'Play'
        if url:
            self.value = url


class Say(TwiML):
    """ <Say> TwiML Verb """

    def __init__(self, message=None, **kwargs):
        super(Say, self).__init__(**kwargs)
        self.name = 'Say'
        if message:
            self.value = message

    def ssml_break(self, strength=None, time=None, **kwargs):
        """
        Create a <Break> element

        :param strength: Set a pause based on strength
        :param time: Set a pause to a specific length of time in seconds or milliseconds, available values: [number]s, [number]ms
        :param kwargs: additional attributes

        :returns: <Break> element
        """
        return self.nest(SsmlBreak(strength=strength, time=time, **kwargs))

    def ssml_emphasis(self, words, level=None, **kwargs):
        """
        Create a <Emphasis> element

        :param words: Words to emphasize
        :param level: Specify the degree of emphasis
        :param kwargs: additional attributes

        :returns: <Emphasis> element
        """
        return self.nest(SsmlEmphasis(words, level=level, **kwargs))

    def ssml_lang(self, words, xml_lang=None, **kwargs):
        """
        Create a <Lang> element

        :param words: Words to speak
        :param xml:lang: Specify the language
        :param kwargs: additional attributes

        :returns: <Lang> element
        """
        return self.nest(SsmlLang(words, xml_lang=xml_lang, **kwargs))

    def ssml_p(self, words, **kwargs):
        """
        Create a <P> element

        :param words: Words to speak
        :param kwargs: additional attributes

        :returns: <P> element
        """
        return self.nest(SsmlP(words, **kwargs))

    def ssml_phoneme(self, words, alphabet=None, ph=None, **kwargs):
        """
        Create a <Phoneme> element

        :param words: Words to speak
        :param alphabet: Specify the phonetic alphabet
        :param ph: Specifiy the phonetic symbols for pronunciation
        :param kwargs: additional attributes

        :returns: <Phoneme> element
        """
        return self.nest(SsmlPhoneme(words, alphabet=alphabet, ph=ph, **kwargs))

    def ssml_prosody(self, words, volume=None, rate=None, pitch=None, **kwargs):
        """
        Create a <Prosody> element

        :param words: Words to speak
        :param volume: Specify the volume, available values: default, silent, x-soft, soft, medium, loud, x-loud, +ndB, -ndB
        :param rate: Specify the rate, available values: x-slow, slow, medium, fast, x-fast, n%
        :param pitch: Specify the pitch, available values: default, x-low, low, medium, high, x-high, +n%, -n%
        :param kwargs: additional attributes

        :returns: <Prosody> element
        """
        return self.nest(SsmlProsody(words, volume=volume, rate=rate, pitch=pitch, **kwargs))

    def ssml_s(self, words, **kwargs):
        """
        Create a <S> element

        :param words: Words to speak
        :param kwargs: additional attributes

        :returns: <S> element
        """
        return self.nest(SsmlS(words, **kwargs))

    def ssml_say_as(self, words, interpret_as=None, role=None, **kwargs):
        """
        Create a <Say-As> element

        :param words: Words to be interpreted
        :param interpret-as: Specify the type of words are spoken
        :param role: Specify the format of the date when interpret-as is set to date
        :param kwargs: additional attributes

        :returns: <Say-As> element
        """
        return self.nest(SsmlSayAs(words, interpret_as=interpret_as, role=role, **kwargs))

    def ssml_sub(self, words, alias=None, **kwargs):
        """
        Create a <Sub> element

        :param words: Words to be substituted
        :param alias: Substitute a different word (or pronunciation) for selected text such as an acronym or abbreviation
        :param kwargs: additional attributes

        :returns: <Sub> element
        """
        return self.nest(SsmlSub(words, alias=alias, **kwargs))

    def ssml_w(self, words, role=None, **kwargs):
        """
        Create a <W> element

        :param words: Words to speak
        :param role: Customize the pronunciation of words by specifying the word’s part of speech or alternate meaning
        :param kwargs: additional attributes

        :returns: <W> element
        """
        return self.nest(SsmlW(words, role=role, **kwargs))


class SsmlW(TwiML):
    """ Improving Pronunciation by Specifying Parts of Speech in <Say> """

    def __init__(self, words, **kwargs):
        super(SsmlW, self).__init__(**kwargs)
        self.name = 'w'
        self.value = words


class SsmlSub(TwiML):
    """ Pronouncing Acronyms and Abbreviations in <Say> """

    def __init__(self, words, **kwargs):
        super(SsmlSub, self).__init__(**kwargs)
        self.name = 'sub'
        self.value = words


class SsmlSayAs(TwiML):
    """ Controlling How Special Types of Words Are Spoken in <Say> """

    def __init__(self, words, **kwargs):
        super(SsmlSayAs, self).__init__(**kwargs)
        self.name = 'say-as'
        self.value = words


class SsmlS(TwiML):
    """ Adding A Pause Between Sentences in <Say> """

    def __init__(self, words, **kwargs):
        super(SsmlS, self).__init__(**kwargs)
        self.name = 's'
        self.value = words


class SsmlProsody(TwiML):
    """ Controling Volume, Speaking Rate, and Pitch in <Say> """

    def __init__(self, words, **kwargs):
        super(SsmlProsody, self).__init__(**kwargs)
        self.name = 'prosody'
        self.value = words


class SsmlPhoneme(TwiML):
    """ Using Phonetic Pronunciation in <Say> """

    def __init__(self, words, **kwargs):
        super(SsmlPhoneme, self).__init__(**kwargs)
        self.name = 'phoneme'
        self.value = words


class SsmlP(TwiML):
    """ Adding a Pause Between Paragraphs in <Say> """

    def __init__(self, words, **kwargs):
        super(SsmlP, self).__init__(**kwargs)
        self.name = 'p'
        self.value = words


class SsmlLang(TwiML):
    """ Specifying Another Language for Specific Words in <Say> """

    def __init__(self, words, **kwargs):
        super(SsmlLang, self).__init__(**kwargs)
        self.name = 'lang'
        self.value = words


class SsmlEmphasis(TwiML):
    """ Emphasizing Words in <Say> """

    def __init__(self, words, **kwargs):
        super(SsmlEmphasis, self).__init__(**kwargs)
        self.name = 'emphasis'
        self.value = words


class SsmlBreak(TwiML):
    """ Adding a Pause in <Say> """

    def __init__(self, **kwargs):
        super(SsmlBreak, self).__init__(**kwargs)
        self.name = 'break'


class Pay(TwiML):
    """ <Pay> Twiml Verb """

    def __init__(self, **kwargs):
        super(Pay, self).__init__(**kwargs)
        self.name = 'Pay'

    def prompt(self, for_=None, error_type=None, card_type=None, attempt=None,
               **kwargs):
        """
        Create a <Prompt> element

        :param for_: Name of the credit card data element
        :param error_type: Type of error
        :param card_type: Type of the credit card
        :param attempt: Current attempt count
        :param kwargs: additional attributes

        :returns: <Prompt> element
        """
        return self.nest(Prompt(
            for_=for_,
            error_type=error_type,
            card_type=card_type,
            attempt=attempt,
            **kwargs
        ))


class Sms(TwiML):
    """ <Sms> TwiML Noun """

    def __init__(self, message, **kwargs):
        super(Sms, self).__init__(**kwargs)
        self.name = 'Sms'
        self.value = message


class Reject(TwiML):
    """ <Reject> TwiML Verb """

    def __init__(self, **kwargs):
        super(Reject, self).__init__(**kwargs)
        self.name = 'Reject'


class Redirect(TwiML):
    """ <Redirect> TwiML Verb """

    def __init__(self, url, **kwargs):
        super(Redirect, self).__init__(**kwargs)
        self.name = 'Redirect'
        self.value = url


class Record(TwiML):
    """ <Record> TwiML Verb """

    def __init__(self, **kwargs):
        super(Record, self).__init__(**kwargs)
        self.name = 'Record'


class Queue(TwiML):
    """ <Queue> TwiML Noun """

    def __init__(self, name, **kwargs):
        super(Queue, self).__init__(**kwargs)
        self.name = 'Queue'
        self.value = name


class Leave(TwiML):
    """ <Leave> TwiML Verb """

    def __init__(self, **kwargs):
        super(Leave, self).__init__(**kwargs)
        self.name = 'Leave'


class Hangup(TwiML):
    """ <Hangup> TwiML Verb """

    def __init__(self, **kwargs):
        super(Hangup, self).__init__(**kwargs)
        self.name = 'Hangup'


class Gather(TwiML):
    """ <Gather> TwiML Verb """

    def __init__(self, **kwargs):
        super(Gather, self).__init__(**kwargs)
        self.name = 'Gather'

    def say(self, message=None, voice=None, loop=None, language=None, **kwargs):
        """
        Create a <Say> element

        :param message: Message to say
        :param voice: Voice to use
        :param loop: Times to loop message
        :param language: Message langauge
        :param kwargs: additional attributes

        :returns: <Say> element
        """
        return self.nest(Say(message=message, voice=voice, loop=loop, language=language, **kwargs))

    def pause(self, length=None, **kwargs):
        """
        Create a <Pause> element

        :param length: Length in seconds to pause
        :param kwargs: additional attributes

        :returns: <Pause> element
        """
        return self.nest(Pause(length=length, **kwargs))

    def play(self, url=None, loop=None, digits=None, **kwargs):
        """
        Create a <Play> element

        :param url: Media URL
        :param loop: Times to loop media
        :param digits: Play DTMF tones for digits
        :param kwargs: additional attributes

        :returns: <Play> element
        """
        return self.nest(Play(url=url, loop=loop, digits=digits, **kwargs))


class Enqueue(TwiML):
    """ <Enqueue> TwiML Noun """

    def __init__(self, name=None, **kwargs):
        super(Enqueue, self).__init__(**kwargs)
        self.name = 'Enqueue'
        if name:
            self.value = name

    def task(self, body, priority=None, timeout=None, **kwargs):
        """
        Create a <Task> element

        :param body: TaskRouter task attributes
        :param priority: Task priority
        :param timeout: Timeout associated with task
        :param kwargs: additional attributes

        :returns: <Task> element
        """
        return self.nest(Task(body, priority=priority, timeout=timeout, **kwargs))


class Task(TwiML):
    """ <Task> TwiML Noun """

    def __init__(self, body, **kwargs):
        super(Task, self).__init__(**kwargs)
        self.name = 'Task'
        self.value = body


class Echo(TwiML):
    """ <Echo> TwiML Verb """

    def __init__(self, **kwargs):
        super(Echo, self).__init__(**kwargs)
        self.name = 'Echo'


class Dial(TwiML):
    """ <Dial> TwiML Verb """

    def __init__(self, number=None, **kwargs):
        super(Dial, self).__init__(**kwargs)
        self.name = 'Dial'
        if number:
            self.value = number

    def client(self, identity=None, url=None, method=None,
               status_callback_event=None, status_callback=None,
               status_callback_method=None, **kwargs):
        """
        Create a <Client> element

        :param identity: Client identity
        :param url: Client URL
        :param method: Client URL Method
        :param status_callback_event: Events to trigger status callback
        :param status_callback: Status Callback URL
        :param status_callback_method: Status Callback URL Method
        :param kwargs: additional attributes

        :returns: <Client> element
        """
        return self.nest(Client(
            identity=identity,
            url=url,
            method=method,
            status_callback_event=status_callback_event,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            **kwargs
        ))

    def conference(self, name, muted=None, beep=None,
                   start_conference_on_enter=None, end_conference_on_exit=None,
                   wait_url=None, wait_method=None, max_participants=None,
                   record=None, region=None, whisper=None, trim=None,
                   status_callback_event=None, status_callback=None,
                   status_callback_method=None, recording_status_callback=None,
                   recording_status_callback_method=None,
                   recording_status_callback_event=None, event_callback_url=None,
                   **kwargs):
        """
        Create a <Conference> element

        :param name: Conference name
        :param muted: Join the conference muted
        :param beep: Play beep when joining
        :param start_conference_on_enter: Start the conference on enter
        :param end_conference_on_exit: End the conferenceon exit
        :param wait_url: Wait URL
        :param wait_method: Wait URL method
        :param max_participants: Maximum number of participants
        :param record: Record the conference
        :param region: Conference region
        :param whisper: Call whisper
        :param trim: Trim the conference recording
        :param status_callback_event: Events to call status callback URL
        :param status_callback: Status callback URL
        :param status_callback_method: Status callback URL method
        :param recording_status_callback: Recording status callback URL
        :param recording_status_callback_method: Recording status callback URL method
        :param recording_status_callback_event: Recording status callback events
        :param event_callback_url: Event callback URL
        :param kwargs: additional attributes

        :returns: <Conference> element
        """
        return self.nest(Conference(
            name,
            muted=muted,
            beep=beep,
            start_conference_on_enter=start_conference_on_enter,
            end_conference_on_exit=end_conference_on_exit,
            wait_url=wait_url,
            wait_method=wait_method,
            max_participants=max_participants,
            record=record,
            region=region,
            whisper=whisper,
            trim=trim,
            status_callback_event=status_callback_event,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            recording_status_callback_event=recording_status_callback_event,
            event_callback_url=event_callback_url,
            **kwargs
        ))

    def number(self, phone_number, send_digits=None, url=None, method=None,
               status_callback_event=None, status_callback=None,
               status_callback_method=None, **kwargs):
        """
        Create a <Number> element

        :param phone_number: Phone Number to dial
        :param send_digits: DTMF tones to play when the call is answered
        :param url: TwiML URL
        :param method: TwiML URL method
        :param status_callback_event: Events to call status callback
        :param status_callback: Status callback URL
        :param status_callback_method: Status callback URL method
        :param kwargs: additional attributes

        :returns: <Number> element
        """
        return self.nest(Number(
            phone_number,
            send_digits=send_digits,
            url=url,
            method=method,
            status_callback_event=status_callback_event,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            **kwargs
        ))

    def queue(self, name, url=None, method=None, reservation_sid=None,
              post_work_activity_sid=None, **kwargs):
        """
        Create a <Queue> element

        :param name: Queue name
        :param url: Action URL
        :param method: Action URL method
        :param reservation_sid: TaskRouter Reservation SID
        :param post_work_activity_sid: TaskRouter Activity SID
        :param kwargs: additional attributes

        :returns: <Queue> element
        """
        return self.nest(Queue(
            name,
            url=url,
            method=method,
            reservation_sid=reservation_sid,
            post_work_activity_sid=post_work_activity_sid,
            **kwargs
        ))

    def sim(self, sim_sid, **kwargs):
        """
        Create a <Sim> element

        :param sim_sid: SIM SID
        :param kwargs: additional attributes

        :returns: <Sim> element
        """
        return self.nest(Sim(sim_sid, **kwargs))

    def sip(self, sip_url, username=None, password=None, url=None, method=None,
            status_callback_event=None, status_callback=None,
            status_callback_method=None, **kwargs):
        """
        Create a <Sip> element

        :param sip_url: SIP URL
        :param username: SIP Username
        :param password: SIP Password
        :param url: Action URL
        :param method: Action URL method
        :param status_callback_event: Status callback events
        :param status_callback: Status callback URL
        :param status_callback_method: Status callback URL method
        :param kwargs: additional attributes

        :returns: <Sip> element
        """
        return self.nest(Sip(
            sip_url,
            username=username,
            password=password,
            url=url,
            method=method,
            status_callback_event=status_callback_event,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            **kwargs
        ))


class Sip(TwiML):
    """ <Sip> TwiML Noun """

    def __init__(self, sip_url, **kwargs):
        super(Sip, self).__init__(**kwargs)
        self.name = 'Sip'
        self.value = sip_url


class Sim(TwiML):
    """ <Sim> TwiML Noun """

    def __init__(self, sim_sid, **kwargs):
        super(Sim, self).__init__(**kwargs)
        self.name = 'Sim'
        self.value = sim_sid


class Number(TwiML):
    """ <Number> TwiML Noun """

    def __init__(self, phone_number, **kwargs):
        super(Number, self).__init__(**kwargs)
        self.name = 'Number'
        self.value = phone_number


class Conference(TwiML):
    """ <Conference> TwiML Noun """

    def __init__(self, name, **kwargs):
        super(Conference, self).__init__(**kwargs)
        self.name = 'Conference'
        self.value = name


class Client(TwiML):
    """ <Client> TwiML Noun """

    def __init__(self, identity=None, **kwargs):
        super(Client, self).__init__(**kwargs)
        self.name = 'Client'
        if identity:
            self.value = identity

    def identity(self, client_identity, **kwargs):
        """
        Create a <Identity> element

        :param client_identity: Identity of the client to dial
        :param kwargs: additional attributes

        :returns: <Identity> element
        """
        return self.nest(Identity(client_identity, **kwargs))

    def parameter(self, name=None, value=None, **kwargs):
        """
        Create a <Parameter> element

        :param name: The name of the custom parameter
        :param value: The value of the custom parameter
        :param kwargs: additional attributes

        :returns: <Parameter> element
        """
        return self.nest(Parameter(name=name, value=value, **kwargs))


class Parameter(TwiML):
    """ <Parameter> TwiML Noun """

    def __init__(self, **kwargs):
        super(Parameter, self).__init__(**kwargs)
        self.name = 'Parameter'


class Identity(TwiML):
    """ <Identity> TwiML Noun """

    def __init__(self, client_identity, **kwargs):
        super(Identity, self).__init__(**kwargs)
        self.name = 'Identity'
        self.value = client_identity


class Connect(TwiML):
    """ <Connect> TwiML Verb """

    def __init__(self, **kwargs):
        super(Connect, self).__init__(**kwargs)
        self.name = 'Connect'

    def room(self, name, participantIdentity=None, **kwargs):
        """
        Create a <Room> element

        :param name: Room name
        :param participantIdentity: Participant identity when connecting to the Room
        :param kwargs: additional attributes

        :returns: <Room> element
        """
        return self.nest(Room(name, participantIdentity=participantIdentity, **kwargs))

    def autopilot(self, name, **kwargs):
        """
        Create a <Autopilot> element

        :param name: Autopilot assistant sid or unique name
        :param kwargs: additional attributes

        :returns: <Autopilot> element
        """
        return self.nest(Autopilot(name, **kwargs))


class Autopilot(TwiML):
    """ <Autopilot> TwiML Noun """

    def __init__(self, name, **kwargs):
        super(Autopilot, self).__init__(**kwargs)
        self.name = 'Autopilot'
        self.value = name


class Room(TwiML):
    """ <Room> TwiML Noun """

    def __init__(self, name, **kwargs):
        super(Room, self).__init__(**kwargs)
        self.name = 'Room'
        self.value = name
