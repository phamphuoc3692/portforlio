from html import escape

# ===== NỘI DUNG (chỉnh sửa ở đây) =====
thong_tin = {
    "badge": "Sẵn sàng nhận dự án mới liên quan đến AI",
    "name": "Phạm Xuân Phước",
    "role": "Frontend Developer / Kỹ sư Phần mềm, Kinh nghiệm 5 năm làm trong lĩnh vực xây dựng",
    "bio": (
        "Tôi tập trung xây dựng các giao diện web tối ưu trải nghiệm người dùng, "
        "tốc độ tải nhanh và dễ bảo trì. Yêu thích việc biến ý tưởng thiết kế "
        "thành sản phẩm chạy mượt mà."
    )
}

ky_nang = {
    "Frontend": ["HTML5", "CSS3", "JavaScript", "React.js", "Tailwind CSS"],
    "Backend & Database": ["Node.js", "Express", "RESTful API", "PostgreSQL", "MongoDB"],
    "Công cụ & Khác": ["Git", "GitHub", "Docker", "Figma", "CI/CD cơ bản"],
}

du_an_tieu_de = "Dự án tiêu biểu"

du_an = [
    {
        "title": "Nền tảng Quản lý Công việc",
        "desc": "Ứng dụng quản lý dự án nội bộ cho đội nhóm với tính năng kéo thả và thông báo thời gian thực.",
        "image": "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?auto=format&fit=crop&w=800&q=80",
        "tags": ["React", "Node.js", "PostgreSQL"],
        "demo": "#",
        "source": "#",
    },
    {
        "title": "Bảng điều khiển Phân tích Dữ liệu",
        "desc": "Website trực quan hóa số liệu tài chính doanh nghiệp với các biểu đồ tương tác thời gian thực.",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "tags": ["JavaScript", "Chart.js", "REST API"],
        "demo": "#",
        "source": "#",
    },
]

lien_he = {
    "contact_title": "Kết nối với tôi",
    "contact_desc": "Bạn đang có dự án cần cộng tác hoặc chỉ đơn giản muốn trao đổi thêm về kỹ thuật? Hãy gửi lời nhắn!",
    "contact_email": "contact@example.com",
    "contact_button": "Gửi tin nhắn",
    "contact_alert": "Đã gửi thông tin!",
}

footer = "© 2026 Phạm Xuân Phước. Thiết kế với HTML và CSS thuần."

# ===== GHÉP VÀO HTML (class lấy từ style.css) =====
def render_projects(projects):
    cards = []
    for i, p in enumerate(projects, 1):
        tags = "\n".join(f"                                <span>{escape(t)}</span>" for t in p["tags"])
        cards.append(
            f"                    <!-- Dự án {i} -->\n"
            f'                    <div class="card project-card">\n'
            f'                        <img src="{escape(p["image"])}" alt="Dự án {i}" class="project-img">\n'
            f'                        <div class="project-body">\n'
            f"                            <h3>{escape(p['title'])}</h3>\n"
            f"                            <p>{escape(p['desc'])}</p>\n"
            f'                            <div class="tags">\n{tags}\n                            </div>\n'
            f'                            <div class="project-links">\n'
            f'                                <a href="{escape(p["demo"])}" target="_blank" class="link-btn">Xem Demo &rarr;</a>\n'
            f'                                <a href="{escape(p["source"])}" target="_blank" class="link-btn text-muted">Mã nguồn</a>\n'
            f"                            </div>\n"
            f"                        </div>\n"
            f"                    </div>"
        )
    return "\n\n".join(cards)



def render_skills(skills):
    cards = []
    for i, (group, items) in enumerate(skills.items(), 1):
        cards.append(
            f"                    <!-- Nhóm {i} -->\n"
            f'                    <div class="card skill-card">\n'
            f"                        <h3>{escape(group)}</h3>\n"
            f'                        <p class="skill-tags">{escape(", ".join(items))}</p>\n'
            f"                    </div>"
        )
    return "\n\n".join(cards)


def build():
    with open("template.html", encoding="utf-8") as f:
        html = f.read()

    values = {k: escape(v) for k, v in thong_tin.items()}
    values["skills"] = render_skills(ky_nang)
    values["projects_title"] = escape(du_an_tieu_de)
    values["projects"] = render_projects(du_an)
    values.update({k: escape(v) for k, v in lien_he.items()})
    values["footer"] = escape(footer)

    for key, val in values.items():
        html = html.replace("{{" + key + "}}", val)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Đã tạo index.html")


if __name__ == "__main__":
    build()
