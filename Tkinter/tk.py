import tkinter as tk
from tkinter import ttk, messagebox

# 예시 문서 데이터
documents = [
    {
        "문서제목": "출퇴근 기록 시스템 개선안",
        "문서개요": "출퇴근 기록 정확도를 높이기 위한 시스템 개선 방안 제안",
        "첨부파일": ["개선안.pdf", "기술사양서.docx"],
        "결재라인": ["팀장", "실장", "이사"],
        "문서목적": "출퇴근 시스템의 효율성 제고",
        "전송정보": "내부 전산망 발송, 2025-05-21 10:00"
    },
    {
        "문서제목": "신규 입사자 교육 자료",
        "문서개요": "신규 입사자 대상 교육 커리큘럼 및 자료 안내",
        "첨부파일": ["교육자료.zip"],
        "결재라인": ["HR팀장", "경영지원본부장"],
        "문서목적": "교육 준비 및 운영",
        "전송정보": "이메일 발송, 2025-05-20 09:30"
    }
]

# 문서 검색 함수 (버튼 클릭용)
def search_document():
    keyword = entry.get().strip().replace(" ", "").lower()
    result_text.delete("1.0", tk.END)
    found = False

    for doc in documents:
        title_clean = doc["문서제목"].replace(" ", "").lower()
        if keyword in title_clean:
            found = True
            result_text.insert(tk.END, f"문서제목: {doc['문서제목']}\n")
            result_text.insert(tk.END, f"문서개요: {doc['문서개요']}\n")
            result_text.insert(tk.END, f"첨부파일: {', '.join(doc['첨부파일'])}\n")
            result_text.insert(tk.END, f"결재라인: {', '.join(doc['결재라인'])}\n")
            result_text.insert(tk.END, f"문서목적: {doc['문서목적']}\n")
            result_text.insert(tk.END, f"전송정보: {doc['전송정보']}\n")
            result_text.insert(tk.END, "-" * 50 + "\n")

    if not found:
        messagebox.showinfo("검색 결과", "해당 문서를 찾을 수 없습니다.")

# 이벤트 핸들러 (Enter 키용)
def search_document_event(event):
    search_document()

# UI 구성
root = tk.Tk()
root.title("문서 검색 앱")

tk.Label(root, text="문서제목으로 검색 (띄어쓰기 무시됨):").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack()

# 엔터 키 이벤트 바인딩 추가
entry.bind("<Return>", search_document_event)

tk.Button(root, text="검색", command=search_document).pack(pady=5)

result_text = tk.Text(root, height=15, width=80)
result_text.pack(pady=10)

root.mainloop()
