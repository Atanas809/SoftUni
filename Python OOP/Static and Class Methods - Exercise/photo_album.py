from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for index, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"

        return "No more free slots"

    def display(self):
        separator = "-" * 11
        result = f"{separator}\n"

        for page in self.photos:
            photo = ["[]" for x in page if x]
            result += f"{' '.join(photo)}\n"
            result += f"{separator}\n"

        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
