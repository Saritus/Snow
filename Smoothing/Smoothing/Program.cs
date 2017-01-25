using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Smoothing
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declaration
            int width = 10;
            int height = 10;
            double[] array = new double[width * height];

            // Initialisation
            Random randNum = new Random();
            for (int i = 0; i < array.Length; i++)
            {
                array[i] = randNum.NextDouble();
            }

            for (int count = 0; count < 30; count++)
            {
                // Printing
                // print_array(array);

                // Smoothing
                array = smooth(array, width, 0.05);
            }
            Console.Read();
        }

        static double[] smooth(double[] array, int width, double p)
        {
            double[] result = new double[array.Length];
            int height = array.Length / width;

            for (int i = 0; i < array.Length; i++)
            {
                // Ecken

                // Oben links
                if (i == 0)
                {
                    result[i] = (1 - 2 * p) * array[i] + p * array[i + 1] + p * array[i + width];
                }

                // Oben rechts
                else if (i == width - 1)
                {
                    result[i] = (1 - 2 * p) * array[i] + p * array[i - 1] + p * array[i + width];
                }

                // Unten links
                else if (i == width * height - width)
                {
                    result[i] = (1 - 2 * p) * array[i] + p * array[i + 1] + p * array[i - width];
                }

                // Unten rechts
                else if (i == width * height - 1)
                {
                    result[i] = (1 - 2 * p) * array[i] + p * array[i - 1] + p * array[i - width];
                }

                // Ränder

                // Oben
                else if (i < width)
                {
                    result[i] = (1 - 3 * p) * array[i] + p * array[i - 1] + p * array[i + 1] + p * array[i + width];
                }

                // Unten
                else if (i > width * height - width)
                {
                    result[i] = (1 - 3 * p) * array[i] + p * array[i - 1] + p * array[i + 1] + p * array[i - width];
                }

                // Links
                else if (i % width == 0)
                {
                    result[i] = (1 - 3 * p) * array[i] + p * array[i + 1] + p * array[i - width] + p * array[i + width];
                }

                // Rechts
                else if (i % width == width - 1)
                {
                    result[i] = (1 - 3 * p) * array[i] + p * array[i - 1] + p * array[i - width] + p * array[i + width];
                }

                // Mitte
                else
                {
                    result[i] = (1 - 4 * p) * array[i] + p * array[i - 1] + p * array[i + 1] + p * array[i - width] + p * array[i + width];
                }

            }

            return result;
        }

        static void print_array(double[] array)
        {
            for (int i = 0; i < array.Length; i++)
            {
                Console.Write("{0:N2} ", array[i]);
            }
            Console.Write("\n");
        }
    }
}
