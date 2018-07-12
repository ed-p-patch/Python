my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
def make_tu(dict):
    new_arr = []
    for k, v in dict.items():
        new_tuple = (k, v)
        new_arr.append(new_tuple)
    print new_arr
make_tu(my_dict)