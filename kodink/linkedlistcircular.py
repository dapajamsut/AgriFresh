class PlaylistYT:
    def __init__(self,idvid,judul,durasi):
        self.idvid = idvid 
        self.judul = judul
        self.durasi = durasi
        self.vidlanjut = None
    
class semuaVid:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_video(self,idvid, judul, durasi):
        vidbaru = PlaylistYT(idvid, judul, durasi)
        if self.head is None:
            self.head = vidbaru
            self.tail = vidbaru
            vidbaru.vidlanjut = self.head
        
        else:
            self.tail.vidlanjut = vidbaru
            self.tail = vidbaru
            self.tail.vidlanjut = self.head
    
    def menampilkan_video(self):
        if self.head is None:
            print("Tidak ada video")
            return
        
        videonow = self.head
        while videonow is not None:
            print(f"video {videonow.idvid}: {videonow.judul} - {videonow.durasi}")
            videonow = videonow.vidlanjut
            if videonow == self.head:
                break
        
    def video_selanjutnya(self, idvid):
        if self.head is None:
            return None

        videonow = self.head
        while True:
            if videonow.idvid == idvid:
                return videonow.vidlanjut
            videonow = videonow.vidlanjut
            if videonow == self.head:
                return None
            
    def video_sebelumnya(self, idvid):
        if self.head is None:
            return None

        videonow = self.head
        videobefore = None

        while True:
            if videonow.idvid == idvid:
                if videobefore is not None:
                    return videobefore
                else:
                    a = videonow
                    while a.vidlanjut != self.head:
                        a = a.vidlanjut
                    return a
            videobefore = videonow
            videonow = videonow.vidlanjut
            if videonow == self.head:
                return None
            
Playlist_YT = semuaVid()

# Menambahkan beberapa video ke playlist
Playlist_YT.tambah_video(1, "Python Lessons", "23:50")
Playlist_YT.tambah_video(2, "C++ Guide", "32:21")
Playlist_YT.tambah_video(3, "Coding for beginner", "15:20")

# Menampilkan semua video yang telah ditambahkan
print("video yang diputar:")
Playlist_YT.menampilkan_video()

# Meminta input dari pengguna tentang nomor video saat ini
videonow = int(input("video ke berapa : "))

# Menampilkan video selanjutnya dan sebelumnya dari video dengan nomor tertentu
print("====== Single Linked List ======")
vidlanjut = Playlist_YT.video_selanjutnya(videonow)
if vidlanjut is not None:
    print(f"video yang di putar setelah video {videonow} adalah: {vidlanjut.judul}")
else:
    print(f"Tidak ada video yang di putar setelah video {videonow}")

print("====== Multiple linked list ======")
videobefore = Playlist_YT.video_sebelumnya(videonow)
if videobefore is not None:
    print(f"video yang di putar sebelum video {videonow} adalah: {videobefore.judul}")
else:
    print(f"tidak ada video yang diputar sebelum video {videonow}")

# Menampilkan video sebelum dan setelah video tertentu menggunakan circular linked list
print("====== Circular linked list ======")
videobefore = Playlist_YT.video_sebelumnya(videonow)
if videobefore is not None:
    print(f"video yang di putar sebelum video {videonow} adalah: {videobefore.judul}")
else:
    print(f"tidak ada video yang diputar sebelum video {videonow}")

vidlanjut = Playlist_YT.video_selanjutnya(videonow)
if vidlanjut is not None:
    print(f"video yang di putar seteleh video {videonow} adalah: {vidlanjut.judul}")
else:
    print(f"Tidak ada video yang di putar setelah video {videonow}")