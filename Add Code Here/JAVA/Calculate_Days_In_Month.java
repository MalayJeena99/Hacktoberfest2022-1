// get the number of days in month
public class Main {
    public static void main(String[] args) {
        System.out.println(getDaysInMonth(1,2020));
    }

    public static boolean isLeapYear(int year){
        if (year > 1 && year <= 9999){
            if (year % 400 == 0 || (year % 100 != 0 && year % 4 == 0)){
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }

    public static int getDaysInMonth(int month, int year){
        if ((month >= 1 && month <= 12) && (year > 1 && year <= 9999 )){

            if (isLeapYear(year)){

                // if year is leap year
                switch (month){
                    case 2:     // february
                        return 29;
                    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                        return 31;
                    default:
                        return 30;
                }
            } else {

                // if year is non-leap year
                switch (month){
                    case 2:
                        return 28;
                    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                        return 31;
                    default:
                        return 30;
                }

            }
        } else {
            return -1;
        }
    }
}