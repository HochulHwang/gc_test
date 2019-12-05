import numpy as np


class CONVERTER_3D_TO_RGB:
  def __init__(self):
    self.w = np.array([[0.5277, 0],
                       [0, -0.8718]], np.float32)
    self.b = np.array([0.5011, 0.5058], np.float32)

  def __call__(
    self,
    _in,  # (... ,3)
  ):
    assert _in.shape[-1] == 3
    _in[..., 0] = np.divide(_in[..., 0], _in[..., 2],
                            where=_in[..., 2] != 0,
                            out=np.zeros_like(_in[..., 2]))
    _in[..., 1] = np.divide(_in[..., 1], _in[..., 2],
                            where=_in[..., 2] != 0,
                            out=np.zeros_like(_in[..., 2]))

    return np.matmul(_in[..., :2], self.w) + self.b


