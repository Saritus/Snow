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

            // Printing
            for (int i = 0; i < array.Length; i++)
            {
                Console.WriteLine(array[i]);
            }
        }

        double[] smooth(double[] array, int width)
        {
            double[] result = (double[])array.Clone();

            //def smooth_array():
            //for i in range(0, width*height):

            //# Ecken
            //# # Oben links
            //if i==0:
            //newarray[i] = (1-2*p)*array[i] + p*array[i+1] + p*array[i+width]
            //# # Oben rechts
            //elif i==width-1:
            //newarray[i] = (1-2*p)*array[i] + p*array[i-1] + p*array[i+width]
            //# # Unten links
            //elif i==width*height-width:
            //newarray[i] = (1-2*p)*array[i] + p*array[i+1] + p*array[i-width]
            //# # Unten rechts
            //elif i==width*height-1:
            //newarray[i] = (1-2*p)*array[i] + p*array[i-1] + p*array[i-width]

            //# Ränder
            //# # Oben
            //elif i<width:
            //newarray[i] = (1-3*p)*array[i] + p*array[i-1] + p*array[i+1] + p*array[i+width]
            //# # Unten
            //elif i>width*height-width:
            //newarray[i] = (1-3*p)*array[i] + p*array[i-1] + p*array[i+1] + p*array[i-width]
            //# # Links
            //elif i%width==0:
            //newarray[i] = (1-3*p)*array[i] + p*array[i+1] + p*array[i-width] + p*array[i+width]
            //# # Rechts
            //elif i%width==width-1:
            //newarray[i] = (1-3*p)*array[i] + p*array[i-1] + p*array[i-width] + p*array[i+width]

            //# Mitte
            //else:
            //newarray[i = (1-4*p)*array[i] + p*array[i-1] + p*array[i+1] + p*array[i-width] + p*array[i+width]

            return result;
        }
    }
}
