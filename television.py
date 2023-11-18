class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the Television instance with default settings: 
        power off, unmuted, volume and channel at minimum."""
        self.__status = False  # TV is initially off
        self.__muted = False   # TV is initially not muted
        self.__volume = Television.MIN_VOLUME  # Set volume to minimum
        self.__channel = Television.MIN_CHANNEL  # Set channel to minimum

    def power(self) -> None:
        """Toggle the power status of the TV."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute status of the TV, only if the TV is on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the TV channel by one. Wraps to MIN_CHANNEL if MAX_CHANNEL is reached."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the TV channel by one. Wraps to MAX_CHANNEL if MIN_CHANNEL is reached."""
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by one step, up to MAX_VOLUME. Unmutes if currently muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

    def volume_down(self) -> None:
        """Decrease the volume by one step, down to MIN_VOLUME. Unmutes if currently muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

    def __str__(self) -> str:
        """Provide a string representation of the current state of the TV."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
