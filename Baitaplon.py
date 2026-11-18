ds = []
FILE = "taikhoan.txt"


# TIM TAI KHOAN
def tim_tk(stk):
    for tk in ds:
        if tk["stk"] == stk:
            return tk
    return None


# NHAP SO TIEN
def nhap_tien(thong_bao):
    while True:
        try:
            tien = float(input(thong_bao))
            if tien > 0:
                return tien
            print("So tien phai lon hon 0!")
        except ValueError:
            print("Vui long nhap so!")


# THEM TAI KHOAN
def them():
    print("\n--- THEM TAI KHOAN ---")
    stk = input("So tai khoan: ").strip()

    if not stk:
        print("So tai khoan khong duoc de trong!")
        return

    if tim_tk(stk):
        print("Tai khoan da ton tai!")
        return

    ten = input("Chu tai khoan: ").strip()
    sdt = input("So dien thoai: ").strip()
    loai = input("Loai tai khoan: ").strip()

    if not ten or not sdt or not loai:
        print("Thong tin khong duoc de trong!")
        return

    sodu = nhap_tien("So du ban dau: ")

    tk = {
        "stk": stk,
        "ten": ten,
        "sdt": sdt,
        "loai": loai,
        "sodu": sodu,
        "tt": "Hoat dong"
    }

    ds.append(tk)
    luu_file()
    print("Them tai khoan thanh cong!")
# HIEN THI TAI KHOAN
def hien_thi():
    print("\n--- DANH SACH TAI KHOAN ---")

    if not ds:
        print("Danh sach trong!")
        return

    print("-" * 100)
    print("{:<12}{:<22}{:<15}{:<15}{:<18}{:<15}".format(
        "So TK", "Chu tai khoan", "Dien thoai",
        "Loai TK", "So du", "Trang thai"))
    print("-" * 100)

    for tk in ds:
        print("{:<12}{:<22}{:<15}{:<15}{:<18,.0f}{:<15}".format(
            tk["stk"], tk["ten"], tk["sdt"],
            tk["loai"], tk["sodu"], tk["tt"]))

    print("-" * 100)


# CAP NHAT TAI KHOAN
def cap_nhat():
    stk = input("Nhap so tai khoan can cap nhat: ").strip()
    tk = tim_tk(stk)

    if tk is None:
        print("Khong tim thay tai khoan!")
        return

    print("Nhap thong tin moi (bo trong neu giu nguyen).")

    ten = input("Chu tai khoan moi: ").strip()
    sdt = input("So dien thoai moi: ").strip()
    loai = input("Loai tai khoan moi: ").strip()

    if ten:
        tk["ten"] = ten
    if sdt:
        tk["sdt"] = sdt
    if loai:
        tk["loai"] = loai

    luu_file()
    print("Cap nhat thanh cong!")


# XOA TAI KHOAN
def xoa():
    stk = input("Nhap so tai khoan can xoa: ").strip()
    tk = tim_tk(stk)

    if tk is None:
        print("Khong tim thay tai khoan!")
        return

    hien_thi_mot(tk)
    xac_nhan = input("Ban co chac chan muon xoa? (y/n): ")

    if xac_nhan.lower() == "y":
        ds.remove(tk)
        luu_file()
        print("Da xoa tai khoan!")
    else:
        print("Da huy thao tac!")
# HIEN THI MOT TAI KHOAN
def hien_thi_mot(tk):
    print("So tai khoan:", tk["stk"])
    print("Chu tai khoan:", tk["ten"])
    print("So dien thoai:", tk["sdt"])
    print("Loai tai khoan:", tk["loai"])
    print("So du:", format(tk["sodu"], ",.0f"))
    print("Trang thai:", tk["tt"])


# TIM KIEM
def tim_kiem():
    tu_khoa = input("Nhap so TK, ten hoac SDT can tim: ").lower()
    tim_thay = False

    for tk in ds:
        if (tu_khoa in tk["stk"].lower()
                or tu_khoa in tk["ten"].lower()
                or tu_khoa in tk["sdt"].lower()):
            hien_thi_mot(tk)
            print("-" * 30)
            tim_thay = True

    if not tim_thay:
        print("Khong tim thay tai khoan!")


# SAP XEP
def sap_xep():
    print("1. Sap xep theo so du")
    print("2. Sap xep theo ten")

    chon = input("Lua chon: ")
    tang = input("Tang dan? (y/n): ").lower() == "y"

    if chon == "1":
        ds.sort(key=lambda tk: tk["sodu"], reverse=not tang)
    elif chon == "2":
        ds.sort(key=lambda tk: tk["ten"].lower(), reverse=not tang)
    else:
        print("Lua chon khong hop le!")
        return

    hien_thi()
    luu_file()


# GUI TIEN
def gui_tien():
    stk = input("Nhap so tai khoan: ").strip()
    tk = tim_tk(stk)

    if tk is None:
        print("Khong tim thay tai khoan!")
        return

    if tk["tt"] != "Hoat dong":
        print("Tai khoan khong hoat dong!")
        return

    tien = nhap_tien("Nhap so tien can gui: ")
    tk["sodu"] += tien

    luu_file()
    print("Gui tien thanh cong!")
    print("So du moi:", format(tk["sodu"], ",.0f"))
    stk1 = input("Tai khoan chuyen: ").strip()
    stk2 = input("Tai khoan nhan: ").strip()

    if stk1 == stk2:
        print("Khong the chuyen tien cho chinh minh!")
        return

    tk1 = tim_tk(stk1)
    tk2 = tim_tk(stk2)

    if tk1 is None or tk2 is None:
        print("Tai khoan chuyen hoac nhan khong ton tai!")
        return

    if tk1["tt"] != "Hoat dong" or tk2["tt"] != "Hoat dong":
        print("Tai khoan khong hoat dong!")
        return

    tien = nhap_tien("Nhap so tien can chuyen: ")

    if tien > tk1["sodu"]:
        print("So du khong du!")
        return

    tk1["sodu"] -= tien
    tk2["sodu"] += tien

    luu_file()
    print("Chuyen tien thanh cong!")

# RUT TIEN
def rut_tien():
    stk = input("Nhap so tai khoan: ").strip()
    tk = tim_tk(stk)

    if tk is None:
        print("Khong tim thay tai khoan!")
        return

    if tk["tt"] != "Hoat dong":
        print("Tai khoan khong hoat dong!")
        return

    tien = nhap_tien("Nhap so tien can rut: ")

    if tien > tk["sodu"]:
        print("So du khong du!")
        return

    tk["sodu"] -= tien

    luu_file()
    print("Rut tien thanh cong!")
    print("So tien da rut:", format(tien, ",.0f"))
    print("So du con lai:", format(tk["sodu"], ",.0f"))
# THONG KE
def thong_ke():
    if not ds:
        print("Danh sach trong!")
        return

    tong = sum(tk["sodu"] for tk in ds)
    trung_binh = tong / len(ds)
    cao_nhat = max(ds, key=lambda tk: tk["sodu"])
    thap_nhat = min(ds, key=lambda tk: tk["sodu"])

    print("\n--- THONG KE TAI KHOAN ---")
    print("Tong so tai khoan:", len(ds))
    print("Tong so du:", format(tong, ",.0f"))
    print("So du trung binh:", format(trung_binh, ",.0f"))

    print("\nTai khoan co so du cao nhat:")
    hien_thi_mot(cao_nhat)

    print("\nTai khoan co so du thap nhat:")
    hien_thi_mot(thap_nhat)


# LUU FILE
def luu_file():
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            for tk in ds:
                dong = "|".join([
                    tk["stk"],
                    tk["ten"],
                    tk["sdt"],
                    tk["loai"],
                    str(tk["sodu"]),
                    tk["tt"]
                ])
                f.write(dong + "\n")

        print("Da luu du lieu vao file!")

    except OSError:
        print("Loi khi ghi file!")


# DOC FILE
def doc_file():
    ds.clear()

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            for dong in f:
                parts = dong.strip().split("|")

                if len(parts) != 6:
                    print("Bo qua dong du lieu khong hop le!")
                    continue

                try:
                    tk = {
                        "stk": parts[0],
                        "ten": parts[1],
                        "sdt": parts[2],
                        "loai": parts[3],
                        "sodu": float(parts[4]),
                        "tt": parts[5]
                    }

                    if not tim_tk(tk["stk"]):
                        ds.append(tk)

                except ValueError:
                    print("Bo qua dong co so du khong hop le!")

        print("Da doc", len(ds), "tai khoan tu file!")

    except FileNotFoundError:
        print("Khong tim thay file taikhoan.txt!")
    except OSError:
        print("Loi khi doc file!")
# MENU CHUYEN TIEN
def menu_giao_dich():
    while True:
        print("\n--- GIAO DICH ---")
        print("1. Gui tien")
        print("2. Rut tien")
        print("3. Chuyen tien")
        print("0. Quay lai")

        chon = input("Nhap lua chon: ")

        if chon == "1":
            gui_tien()
        elif chon == "2":
            rut_tien()
        elif chon == "3":
            chuyen_tien()
        elif chon == "0":
            break
        else:
            print("Lua chon khong hop le!")


# MENU CHINH
def menu():
    while True:
        print("\n========== QUAN LY TAI KHOAN NGAN HANG ==========")
        print("1. Them tai khoan")
        print("2. Hien thi danh sach")
        print("3. Cap nhat tai khoan")
        print("4. Xoa tai khoan")
        print("5. Tim kiem tai khoan")
        print("6. Sap xep tai khoan")
        print("7. Giao dich")
        print("8. Thong ke")
        print("9. Luu file")
        print("10. Doc lai file")
        print("0. Thoat")
        print("================================================")

        chon = input("Nhap lua chon: ")

        if chon == "1":
            them()
        elif chon == "2":
            doc_file()
            hien_thi()
        elif chon == "3":
            cap_nhat()
        elif chon == "4":
            xoa()
        elif chon == "5":
            tim_kiem()
        elif chon == "6":
            sap_xep()
        elif chon == "7":
            menu_giao_dich()
        elif chon == "8":
            thong_ke()
        elif chon == "9":
            luu_file()
        elif chon == "10":
            doc_file()
        elif chon == "0":
            luu_file()
            print("Cam on ban da su dung chuong trinh!")
            break
        else:
            print("Lua chon khong hop le!")


# CHAY CHUONG TRINH
doc_file()
menu()