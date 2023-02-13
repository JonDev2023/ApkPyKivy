import apk_py_kivy

print('ApkPyKivy Development Console')

while True:
    text = input('apk-py-kivy > ')
    result, error = apk_py_kivy.run('<stdin>', text)
    if error: print(error.as_string())
    else: print(result)