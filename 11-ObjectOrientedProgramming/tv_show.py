# tv_show.py file
# main program
import tv

def main():
   # object creation
   my_tv = tv.TV()
   my_tv.show_status()
   
   my_tv.turn_on()
   my_tv.show_status()
   my_tv.set_channel(5)
   my_tv.show_status()
   my_tv.turn_off()
   my_tv.show_status()
   # object usage
if __name__ == "__main__":
   main() 