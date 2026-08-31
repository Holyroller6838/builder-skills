class ProfileNotFoundError(Exception):
    def __init__(self, profile_name: str):
        super().__init__(f"unknown readiness profile: {profile_name!r}")
        self.profile_name = profile_name


class MalformedPayloadError(Exception):
    pass
