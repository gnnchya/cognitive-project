import onnx

# Preprocessing: load the ONNX model
model_path = "/Users/gnnchya/Documents/cognitive-keras/model4.onnx"
onnx_model = onnx.load(model_path)

print(f"The model is:\n{onnx_model}")

# Check the model
try:
    onnx.checker.check_model(onnx_model)
except onnx.checker.ValidationError as e:
    print(f"The model is invalid: {e}")
else:
    print("The model is valid!")