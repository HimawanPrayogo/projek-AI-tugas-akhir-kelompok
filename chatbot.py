import nltk
from nltk.chat.util import Chat, reflections
import re
import tkinter as tk
from tkinter import scrolledtext

# Data kelas dan tugas
kelas = {
    "pendidikan pancasila": {
        "tugas": {
            "tugas pemilu": {
                "deskripsi": "Silahkan baca petunjuk terlampir\nKetentuan tugas:\n- Tugas terakhir dikumpulkan tanggal 15 Februari 2024 15:00 WIB\n- Tugas dikumpulkan melalui situs e-class dengan mengirimkan file\n- Tugas tidak bisa dikumpul ulang\n- Tugas masih bisa dikumpulkan setelah tanggal berakhir dengan resiko pengurangan nilai",
                "deadline": "15 Februari 2024",
            },
            "tm 6 sebagai pendidikan pancasila": {
                "deskripsi": "Diskusikan pentingnya Pancasila dalam kehidupan berbangsa dan bernegara.",
                "deadline": "20 Maret 2024",
            },
            "uts": {
                "deskripsi": "Ujian Tengah Semester untuk Pendidikan Pancasila.",
                "deadline": "10 April 2024",
            },
            "tugas kelompok sila 1": {
                "deskripsi": "Presentasi mengenai Sila Pertama Pancasila.",
                "deadline": "5 Mei 2024",
            },
            "tugas kelompok sila kedua": {
                "deskripsi": "Analisis penerapan Sila Kedua dalam masyarakat.",
                "deadline": "12 Mei 2024",
            },
            "tugas kelompok sila ketiga": {
                "deskripsi": "Makalah tentang pentingnya persatuan dalam Sila Ketiga.",
                "deadline": "19 Mei 2024",
            },
            "pr kelompok": {
                "deskripsi": "Pekerjaan rumah mengenai materi yang dibahas minggu ini.",
                "deadline": "26 Mei 2024",
            },
            "tugas kelompok sila 4": {
                "deskripsi": "Diskusi kelompok tentang penerapan demokrasi dalam Sila Keempat.",
                "deadline": "2 Juni 2024",
            }
        }
    },
    "pemrograman web": {
        "tugas": {
            "tugas aktivitas kelas 1": {
                "deskripsi": "Buat halaman web statis menggunakan HTML dan CSS.",
                "deadline": "25 Februari 2024",
            },
            "tugas 2": {
                "deskripsi": "Implementasi JavaScript untuk interaktifitas pada halaman web.",
                "deadline": "5 Maret 2024",
            },
            "midterm project": {
                "deskripsi": "Proyek tengah semester yang mencakup penggunaan HTML, CSS, dan JavaScript.",
                "deadline": "20 Maret 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir semester berupa aplikasi web sederhana.",
                "deadline": "15 Mei 2024",
            }
        }
    },
    "praktikum pemrograman web": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Instalasi dan konfigurasi server web lokal.",
                "deadline": "28 Februari 2024",
            },
            "tugas 2": {
                "deskripsi": "Membuat halaman web dengan backend sederhana menggunakan PHP.",
                "deadline": "10 Maret 2024",
            },
            "tugas 3": {
                "deskripsi": "Koneksi database MySQL dengan PHP.",
                "deadline": "25 Maret 2024",
            }
        }
    },
    "kecerdasan buatan": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Membuat program sederhana yang menerapkan algoritma pencarian.",
                "deadline": "1 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Implementasi jaringan saraf tiruan untuk klasifikasi data.",
                "deadline": "15 Maret 2024",
            },
            "project akhir": {
                "deskripsi": "Proyek akhir mengenai aplikasi kecerdasan buatan dalam kehidupan nyata.",
                "deadline": "20 Mei 2024",
            }
        }
    },
    "keamanan komputer": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Analisis serangan malware dan cara pencegahannya.",
                "deadline": "5 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Implementasi firewall dan IDS untuk proteksi jaringan.",
                "deadline": "20 Maret 2024",
            },
            "final exam": {
                "deskripsi": "Ujian akhir mengenai topik-topik keamanan komputer.",
                "deadline": "30 Mei 2024",
            }
        }
    },
    "etika profesi teknologi informasi": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Makalah tentang etika dalam penggunaan data pribadi.",
                "deadline": "10 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Presentasi tentang kode etik profesi di bidang TI.",
                "deadline": "25 Maret 2024",
            },
            "project kelompok": {
                "deskripsi": "Proyek kelompok mengenai kasus etika dalam teknologi informasi.",
                "deadline": "10 Mei 2024",
            }
        }
    },
    "rekayasa perangkat lunak beriorientasi obyek": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Implementasi dasar OOP dalam bahasa pemrograman pilihan.",
                "deadline": "12 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Desain dan implementasi pola desain dalam proyek kecil.",
                "deadline": "25 Maret 2024",
            },
            "tugas akhir": {
                "deskripsi": "Proyek akhir yang mencakup seluruh konsep OOP yang dipelajari.",
                "deadline": "5 Mei 2024",
            }
        }
    },
    "praktikum rekayasa perangkat lunak beriorientasi obyek": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Praktikum dasar-dasar OOP.",
                "deadline": "15 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Praktikum implementasi pola desain.",
                "deadline": "30 Maret 2024",
            },
            "proyek praktikum": {
                "deskripsi": "Proyek praktikum akhir semester.",
                "deadline": "20 Mei 2024",
            }
        }
    },
    "data warehouse": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Desain skema data warehouse untuk perusahaan retail.",
                "deadline": "20 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Implementasi ETL process untuk data warehouse.",
                "deadline": "10 April 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir berupa implementasi data warehouse lengkap.",
                "deadline": "25 Mei 2024",
            }
        }
    },
    "sistem informasi geografis": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Pemetaan data menggunakan software GIS.",
                "deadline": "12 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Analisis data spasial untuk kasus studi tertentu.",
                "deadline": "25 Maret 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir berupa analisis dan visualisasi data geografis.",
                "deadline": "5 Mei 2024",
            }
        }
    },
    "machine learning": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Implementasi model regresi linear sederhana.",
                "deadline": "15 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Klasifikasi data menggunakan algoritma KNN.",
                "deadline": "30 Maret 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir berupa aplikasi machine learning untuk kasus nyata.",
                "deadline": "20 Mei 2024",
            }
        }
    },
    "big data": {
        "tugas": {
            "tugas 1": {
                "deskripsi": "Pengolahan data besar menggunakan Hadoop.",
                "deadline": "10 Maret 2024",
            },
            "tugas 2": {
                "deskripsi": "Analisis data besar menggunakan Apache Spark.",
                "deadline": "25 Maret 2024",
            },
            "final project": {
                "deskripsi": "Proyek akhir berupa analisis big data untuk kasus bisnis tertentu.",
                "deadline": "15 Mei 2024",
            }
        }
    }
}







# Fungsi untuk mengambil tugas berdasarkan nama kelas
def get_tugas(kelas_name):
    if kelas_name in kelas:
        tugas_list = kelas[kelas_name]["tugas"]
        tugas_str = "\n".join(f"{i+1}. {tugas}" for i, tugas in enumerate(tugas_list))
        return f"Berikut adalah daftar tugas untuk {kelas_name}:\n{tugas_str}"
    else:
        return "Kelas tidak ditemukan."

# Fungsi untuk mendapatkan deskripsi dan deadline tugas
def get_tugas_detail(kelas_name, tugas_name):
    if kelas_name in kelas:
        tugas_list = kelas[kelas_name]["tugas"]
        if tugas_name in tugas_list:
            tugas = tugas_list[tugas_name]
            deskripsi = tugas.get("deskripsi", "Deskripsi tidak tersedia.")
            deadline = tugas.get("deadline", "Deadline tidak tersedia.")
            return f"Detail untuk tugas {tugas_name} di kelas {kelas_name}:\nDeskripsi: {deskripsi}\nDeadline: {deadline}"
        else:
            return f"Tugas {tugas_name} tidak ditemukan di kelas {kelas_name}."
    else:
        return "Kelas tidak ditemukan."


# Fungsi untuk mendapatkan daftar kelas yang ada
def get_kelas_list():
    kelas_list = "\n".join(kelas.keys())
    return f"Berikut adalah daftar kelas yang Anda ambil:\n{kelas_list}"



def respond_to_input(user_input):
    for pattern, response in patterns.items():
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            if callable(response):
                return response(match.groups())
            else:
                return response
    return "Maaf, saya tidak mengerti. Bisakah kamu mengulanginya?"


def chatbot_conversation():
    def send_message(event=None):
        user_input = entry.get().strip()
        if user_input.lower() == 'bye':
            window.quit()
        response = respond_to_input(user_input)
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Anda: " + user_input + "\n")
        chat_area.insert(tk.END, "Chatbot: " + response + "\n\n")
        chat_area.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

    window = tk.Tk()
    window.title("Chatbot")

    chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(window, width=80)
    entry.pack(padx=10, pady=10, fill=tk.X)
    entry.bind("<Return>", send_message)

    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack(padx=10, pady=10)

    window.mainloop()


patterns = {
    r"(?:apa saja|sebutkan|daftar) kelas(?: yang)? ada": lambda matches: get_kelas_list(),
    r"(?:apa saja|sebutkan|daftar|apa) kelas?": lambda matches: get_kelas_list(),
    r"(?:apa saja|sebutkan|daftar) kelas(?: yang)? tersedia": lambda matches: get_kelas_list(),
    r"(?:apa saja|sebutkan|daftar) (?:tugas|PR)(?: untuk| di)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"(?:tugas|pekerjaan rumah|PR) apa(?: yang| saja yang) diberikan(?: di| untuk)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"(?:detail|informasi tentang|info tentang|info detail tentang) (.*) (?:tugas|pekerjaan rumah|PR) (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:detail|informasi tentang|info tentang|info detail tentang) (?:tugas|pekerjaan rumah|PR) (.*) (?:untuk|di)? (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"tugas apa(?: untuk| di)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"apa detail (?:tugas|pekerjaan rumah|PR) (.*) (?:untuk|di)? (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:informasi|detail|deskripsi) tentang (.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:halo|hai|hey) (?:bot|chatbot|teman)": ["Halo! Ada yang bisa saya bantu?"],
    r"sampai jumpa|bye|selamat tinggal": ["Sampai jumpa!", "Selamat tinggal!", "Bye!"],
    r"(?:terima kasih|thanks)": ["Sama-sama! Ada yang lain yang bisa saya bantu?"],
    r"(.*)": ["Maaf, saya tidak mengerti. Bisakah kamu mengulanginya?"],
     r"(?:apa saja|sebutkan|daftar) (?:tugas|PR)(?: untuk| di)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"(?:tugas|pekerjaan rumah|PR) apa(?: yang| saja yang) diberikan(?: di| untuk)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"(?:detail|informasi tentang|info tentang|info detail tentang) (.*) (?:tugas|pekerjaan rumah|PR) (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:detail|informasi tentang|info tentang|info detail tentang) (?:tugas|pekerjaan rumah|PR) (.*) (?:untuk|di)? (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"tugas apa(?: untuk| di)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"apa detail (?:tugas|pekerjaan rumah|PR) (.*) (?:untuk|di)? (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:informasi|detail|deskripsi) tentang (.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:halo|hai|hey) (?:bot|chatbot|teman)": ["Halo! Ada yang bisa saya bantu?"],
    r"(?:apa saja|sebutkan|daftar) kelas(?: yang)? ada": lambda matches: get_kelas_list(),
    r"sampai jumpa|bye|selamat tinggal": ["Sampai jumpa!", "Selamat tinggal!", "Bye!"],
    r"(?:terima kasih|thanks)": ["Sama-sama! Ada yang lain yang bisa saya bantu?"],
    r"(.*)": ["Maaf, saya tidak mengerti. Bisakah kamu mengulanginya?"],
    r"(?:apa saja|sebutkan|daftar) (?:tugas|PR)(?: untuk| di)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"(?:tugas|pekerjaan rumah|PR) apa(?: yang| saja yang) diberikan(?: di| untuk)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"(?:detail|informasi tentang|info tentang|info detail tentang) (.*) (?:tugas|pekerjaan rumah|PR) (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:detail|informasi tentang|info tentang|info detail tentang) (?:tugas|pekerjaan rumah|PR) (.*) (?:untuk|di)? (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"tugas apa(?: untuk| di)? (.*)": lambda matches: get_tugas(matches[0].strip().lower()),
    r"apa detail (?:tugas|pekerjaan rumah|PR) (.*) (?:untuk|di)? (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:informasi|detail|deskripsi) tentang (.*) di (.*)": lambda matches: get_tugas_detail(matches[1].strip().lower(), matches[0].strip().lower()),
    r"(?:halo|hai|hey) (?:bot|chatbot|teman)": ["Halo! Ada yang bisa saya bantu?"],
    r"(?:apa saja|sebutkan|daftar) kelas(?: yang)? ada": lambda matches: get_kelas_list(),
    r"sampai jumpa|bye|selamat tinggal": ["Sampai jumpa!", "Selamat tinggal!", "Bye!"],
    r"(?:terima kasih|thanks)": ["Sama-sama! Ada yang lain yang bisa saya bantu?"],
    r"(.*)": ["Maaf, saya tidak mengerti. Bisakah kamu mengulanginya?"],
    r"(?:apa saja|sebutkan|daftar) kelas(?: yang)? ada": lambda matches: get_kelas_list(),
    r"(?:apa saja|sebutkan|daftar) kelas(?: yang)? saya ambil": lambda matches: get_kelas_saya(),
}


def get_kelas_saya():
    # Simpan daftar kelas yang Anda ambil di variabel atau database
    kelas_saya = ["Pendidikan Pancasila", "Pemrograman Web", "Keamanan Komputer", "Machine Learning"]  # Contoh daftar kelas Anda

    kelas_list = "\n".join(kelas_saya)
    return f"Anda telah mengambil kelas-kelas berikut:\n{kelas_list}"



# Fungsi untuk mengolah respon
def respond_to_input(user_input):
    for pattern, responses in patterns.items():
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            response = responses
            if callable(response):
                return response(match.groups())
            else:
                return response[0]
    return "Maaf, saya tidak mengerti. Bisakah kamu mengulanginya?"

# Fungsi untuk memulai percakapan dengan chatbot menggunakan GUI
def chatbot_conversation():
    def send_message(event=None):
        user_input = entry.get()
        if user_input.lower() == 'bye':
            window.quit()
        response = respond_to_input(user_input)
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, "Anda: " + user_input + "\n")
        chat_area.insert(tk.END, "Chatbot: " + response + "\n\n")
        chat_area.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

    # Create the main window
    window = tk.Tk()
    window.title("Chatbot")

    # Create a chat area
    chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create an entry box for user input
    entry = tk.Entry(window, width=80)
    entry.pack(padx=10, pady=10, fill=tk.X)
    entry.bind("<Return>", send_message)  # Bind the Return key to send the message

    # Create a send button
    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.pack(padx=10, pady=10)

    # Start the GUI event loop
    window.mainloop()

# Memulai percakapan
if __name__ == "__main__":
    chatbot_conversation()
