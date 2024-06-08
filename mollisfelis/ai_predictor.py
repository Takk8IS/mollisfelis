# mollisfelis/ai_predictor.py

import numpy as np
from scipy.interpolate import interp1d

class AnimationModel:
    def __init__(self, easing_functions):
        self.easing_functions = easing_functions
        self.model = None

    def train(self, X, y):
        self.model = interp1d(X, y, kind='cubic', axis=0)

    def predict(self, X):
        if self.model is None:
            raise ValueError("Model not trained. Call 'train' method first.")
        return self.model(X)

    def smooth_animation(self, keyframes, duration, fps=60, easing_func=None):
        if easing_func is None:
            easing_func = np.random.choice(self.easing_functions)

        times = np.linspace(0, duration, len(keyframes))
        self.train(times, keyframes)

        frames = np.linspace(0, duration, int(duration * fps))
        animated_frames = self.predict(frames)

        eased_frames = np.array([easing_func(t / duration) for t in frames])
        smoothed_frames = animated_frames * eased_frames[:, np.newaxis]

        return smoothed_frames

    def save_animation(self, frames, output_file):
        np.save(output_file, frames)

    def load_animation(self, input_file):
        return np.load(input_file)

def ease_linear(t):
    return t

def ease_in_quad(t):
    return t**2

def ease_out_quad(t):
    return 1 - (1 - t)**2

def ease_in_out_quad(t):
    return 2*t**2 if t < 0.5 else 1 - (-2*t + 2)**2 / 2

def main():
    easing_functions = [ease_linear, ease_in_quad, ease_out_quad, ease_in_out_quad]
    model = AnimationModel(easing_functions)

    keyframes = np.array([[0, 0], [1, 1], [2, 0], [3, 1]])
    duration = 3
    fps = 60

    smoothed_frames = model.smooth_animation(keyframes, duration, fps)
    model.save_animation(smoothed_frames, "animation.npy")

    loaded_frames = model.load_animation("animation.npy")
    print("Smoothed animation frames:")
    print(loaded_frames)

if __name__ == "__main__":
    main()
