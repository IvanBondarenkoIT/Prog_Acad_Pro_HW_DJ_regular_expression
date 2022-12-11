'''
Домашнє завдання:
1. Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R,
 за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
2. Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
3. Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
Вимоги:
-Цифри (0-9).
-лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
-у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
-Символ "-" не може повторюватися.
4. Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів,
 що містить лише літери та цифри.
'''
import re


def find_all_inclusion(txt, pattern):
    return re.findall(pattern=pattern, string=txt)


def find_inclusion(txt, pattern):
    match = re.search(pattern=pattern, string=txt)
    if match:
        return match.group()
    else:
        return None


text = "Rbr RRbr Rr Rbbr Rbbbr Rbb bbr"
print(find_all_inclusion(text, r"Rb+r"))
text = "9979-99999999 9999"
print(find_inclusion(text, r"(\d{4}(-| |:)?){4}"))
text = "sd7sddfs-Rf@dfssdf.dsf"
print(find_inclusion(text, r"([A-z]+)-?(\S+)[@]\S+[.]...$"))
text = "ds-fT4"
print(find_inclusion(text, r"\w{2,10}"))
