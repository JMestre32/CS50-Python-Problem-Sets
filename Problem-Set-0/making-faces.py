def main():
    face = input("Type a smiling, :), or sad, :(, face to be converted into an emoji ")
    face = convert(face)
    print(face)

def convert(f):
    #My first approach (this is wrong because it doesn't produce the desired output)
        # match f:
        #     case ":)" | "(:" :
        #         return "🙂"
        #     case ":(" | "):":
        #         return ""
        #     case _:
        #         return "bro?"
    #Alternate approach (Correct)
    ans = f.replace(":)", "🙂")
    ans2 = ans.replace(":(", "🙁")
    return ans2



main()