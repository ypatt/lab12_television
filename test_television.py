import pytest
from television import Television

# Test for initial state of the Television
def test_initial_state():
    tv = Television()
    assert not tv._Television__status, "TV should be initially off"
    assert not tv._Television__muted, "TV should be initially unmuted"
    assert tv._Television__volume == Television.MIN_VOLUME, "Initial volume should be at minimum"
    assert tv._Television__channel == Television.MIN_CHANNEL, "Initial channel should be at minimum"

# Test for power toggle functionality
def test_power_toggle():
    tv = Television()
    tv.power()
    assert tv._Television__status, "TV should be on after toggling power"
    tv.power()
    assert not tv._Television__status, "TV should be off after toggling power again"

# Test for mute and unmute functionality
def test_mute_unmute():
    tv = Television()
    tv.power()  # Turn on TV
    tv.mute()
    assert tv._Television__muted, "TV should be muted"
    tv.mute()
    assert not tv._Television__muted, "TV should be unmuted"

# Test for channel up functionality
def test_channel_up():
    tv = Television()
    tv.power()  # Turn on TV
    initial_channel = tv._Television__channel
    tv.channel_up()
    assert tv._Television__channel == initial_channel + 1, "Channel should increase by 1"
    # Test wrapping to MIN_CHANNEL from MAX_CHANNEL
    tv._Television__channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._Television__channel == Television.MIN_CHANNEL, "Channel should wrap to minimum"

# Test for channel down functionality
def test_channel_down():
    tv = Television()
    tv.power()  # Turn on TV
    initial_channel = tv._Television__channel
    tv.channel_down()
    # Test wrapping to MAX_CHANNEL from MIN_CHANNEL
    if initial_channel == Television.MIN_CHANNEL:
        assert tv._Television__channel == Television.MAX_CHANNEL, "Channel should wrap to maximum"
    else:
        assert tv._Television__channel == initial_channel - 1, "Channel should decrease by 1"

# Test for volume up functionality
def test_volume_up():
    tv = Television()
    tv.power()  # Turn on TV
    initial_volume = tv._Television__volume
    tv.volume_up()
    if initial_volume < Television.MAX_VOLUME:
        assert tv._Television__volume == initial_volume + 1, "Volume should increase by 1"
    else:
        assert tv._Television__volume == Television.MAX_VOLUME, "Volume should remain at maximum"

# Test for volume down functionality
def test_volume_down():
    tv = Television()
    tv.power()  # Turn on TV
    initial_volume = tv._Television__volume
    tv.volume_down()
    if initial_volume > Television.MIN_VOLUME:
        assert tv._Television__volume == initial_volume - 1, "Volume should decrease by 1"
    else:
        assert tv._Television__volume == Television.MIN_VOLUME, "Volume should remain at minimum"
