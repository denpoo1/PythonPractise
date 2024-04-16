import cv2

def create_meme(path_to_image, meme_text):
    original_image = cv2.imread(path_to_image)

    img_height, img_width = original_image.shape[:2]
    img_with_border = cv2.copyMakeBorder(original_image, 0, 100, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    font_style = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_with_border, meme_text, (10, img_height + 50), font_style, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Meme", img_with_border)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    user_input = input("Podaj numer obrazka (np. 1, 2, 3, 4, 5): ")
    path_to_image = f"images/meme{user_input}.jpg"
    meme_text = input("Wpisz tekst do wyświetlenia na memie: ")
    create_meme(path_to_image, meme_text)