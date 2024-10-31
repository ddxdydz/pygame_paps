from basic.general_settings import FPS


class GameAnimatedObject:
    DEFAULT_STAGE = "default"
    DEFAULT_DESCRIPTION = {
        DEFAULT_STAGE: {
            "frames": ["error1_image", "error2_image", "error3_image"],
            "frames_per_second": 5, "priority": 0, "end_cycle_stage": DEFAULT_STAGE, "require_reset": False
        }
    }

    def __init__(self, current_stage=None, animation_description: dict = None):
        self.current_stage = GameAnimatedObject.DEFAULT_STAGE if current_stage is None else current_stage
        self.animation_description = GameAnimatedObject.DEFAULT_DESCRIPTION \
            if animation_description is None else animation_description

        self.current_delay = 0
        self.current_frame_index = 0
        self.stage_updating_delay = 0  # frames

        # Tracking the end of stage
        self.previous_stage = self.current_stage
        self.is_first_frame = False

    def _get_frames_count(self, stage):
        return len(self.animation_description[stage]["frames"])

    def _get_stage_priority(self, stage):
        return self.animation_description[stage]["priority"]

    def _get_stage_speed(self, stage):
        return self.animation_description[stage]["frames_per_second"]

    def _process_stage_ending(self):
        if self.current_frame_index == self._get_frames_count(self.current_stage):
            self.previous_stage = self.current_stage
            self.is_first_frame = True
            self.current_stage = self.animation_description[self.current_stage]["end_cycle_stage"]
            self.current_frame_index = 0

    def _is_priority_stage(self, new_stage):
        if self._get_stage_priority(new_stage) < self._get_stage_priority(self.current_stage):
            return False
        return True

    def change_stage(self, new_stage):
        if self._is_priority_stage(new_stage):
            self.current_stage = new_stage
            self.current_frame_index %= self._get_frames_count(self.current_stage)
            if self.animation_description[new_stage]["require_reset"]:
                self.current_frame_index = 0

    def check_stage_end(self, stage):
        if self.previous_stage == stage and self.is_first_frame:
            return True
        return False

    def update_frame(self):
        self.is_first_frame = False
        self.current_delay -= 1 / FPS
        if self.current_delay < 0:
            self.current_delay = 1 / self._get_stage_speed(self.current_stage)
            self.current_frame_index += 1
        self._process_stage_ending()

    def get_frame_code(self) -> "str":
        return self.animation_description[self.current_stage]["frames"][self.current_frame_index]
