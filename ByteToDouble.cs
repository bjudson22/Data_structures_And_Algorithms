using System;

namespace ConsoleApp3
{
    class Program
    {
        static void Main(string[] args)
        {
            string number = "1.0023";
            double answer = convertString(number);
            Console.WriteLine(answer);
        }
        static double convertString(string number)
        {
            int i = 0;
            int before = 0;
            double answer = 0;
            while (number[i] != '.')
            {
                before++;
                i++;
            }
            i = 0;
            while (before > 0)
            {
                answer += (number[i] - 48) * (Math.Pow((10), before - 1));
                before--;
                i++;
            }
            int after = 1;
            i++;
            while (i < number.Length)
            {
                if (number[i] == '0')
                {
                    i++;
                    after++;
                    continue;
                }
                answer += (number[i] - 48) * (Math.Pow((10), -after));
                after++;
                i++;
            }
            return answer;
        }
    }
}