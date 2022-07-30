from tkinter import *
import Editor
import Inference

window = Tk()
window.title('Knowledge Inference System')
window.geometry('300x150')

Editor_Btn = Button(window, width=25, text='Knowledge Base Editor',command=Editor.fEditor)
Editor_Btn.pack(pady=30)

Inference_Btn = Button(window, width=25, text='Knowledge Inference Engine',command=Inference.fInference)
Inference_Btn.pack()

window.mainloop()


# tkinter ใช้ทำ graphic user interface
# import editor (เรียกใช้ไฟล์ editor)
# import Inference (เรียกใช้ไฟล์ Inference)
# สร้าง window และเขียน title  
#     window = Tk()
#     window.title('Knowledge Inference System')
#     window.geometry('300x150')
# สร้าง ปุ่ม และเมื่อกดเรียกใช้ function editor จาก ไฟล์ editor
#     Editor_Btn = Button(window, width=25, text='Knowledge Base Editor',command=Editor.fEditor)
#     Editor_Btn.pack(pady=30)
#     Inference_Btn = Button(window, width=25, text='Knowledge Inference Engine',command=Inference.fInference)
#     Inference_Btn.pack()