# Система для автоматического оценивания письменной части ЕГЭ

Готовая к работе система распознавания лежит в [данном файле](https://github.com/d-asv-b/MAI_OCR_Practice_2025/blob/main/YOLO_Detection_%26_Evaluation.ipynb).

Для корректной работы системы нужны изображения работы и JSON файлы с распознанным текстом для каждой страницы. Также необходим API-ключ для [Google AI Studio](https://aistudio.google.com/apikey).

Пример обработки заданий:

1) Определение границ заданий на изображении:
<img width="2310" height="2590" alt="image" src="https://github.com/user-attachments/assets/cbd9e8d1-cd2c-4cbc-b6ca-00969f0e7c64" />

2) Сопоставление номеров заданий распознанному тексту:
<img width="664" height="643" alt="image" src="https://github.com/user-attachments/assets/c3c1c0d8-b43c-4b66-a31f-57a6921c5f9c" />

3) Оценка заданий с помощью LLM:
<img width="1829" height="625" alt="image" src="https://github.com/user-attachments/assets/a2181799-224c-427c-b836-fec294db5be5" />
<img width="672" height="159" alt="image" src="https://github.com/user-attachments/assets/0c8f68b3-5a4d-4e2e-96c8-b623d80f4b33" />
