import cv2


def sequential(vid_path, frame_indices):
  cap = cv2.VideoCapture(vid_path)
  frames = []
  num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
  for frame_idx in range(num_frames):
    cap.grab()
    if frame_idx not in frame_indices:
      continue
    ret, frame = cap.retrieve()

    if ret:
      frames.append(frame)
    else:
      raise RuntimeError(vid_path)
    # frame_indices.pop(0)
    if len(frame_indices) == len(frames):
      break
  cap.release()
  return frames


def sequential_dict(vid_path, frame_indices):
  cap = cv2.VideoCapture(vid_path)
  frames = {}
  frame_indices = set(frame_indices)
  num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
  for frame_idx in range(num_frames):
    cap.grab()
    if frame_idx not in frame_indices:
      continue
    ret, frame = cap.retrieve()

    if ret:
      frames[frame_idx] = frame
    else:
      raise RuntimeError(vid_path)
    # frame_indices.pop(0)
    if len(frame_indices) == len(frames):
      break
  cap.release()
  return frames


def random(vid_path, frame_indices):
  cap = cv2.VideoCapture(vid_path)
  frames = []
  for frame_idx in frame_indices:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if ret:
      frames.append(frame)
    else:
      raise RuntimeError
  cap.release()
  return frames

