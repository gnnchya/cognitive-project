import tflite2onnx

tflite_path = '/Users/gnnchya/Documents/cognitive-keras/android.tflite'
onnx_path = '/Users/gnnchya/Documents/cognitive-keras/model3.onnx'

tflite2onnx.convert(tflite_path, onnx_path)