{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ce0852b",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'school_tools'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m school_tools \u001b[38;5;28;01mimport\u001b[39;00m average, grade, report\n\u001b[32m      2\u001b[39m \n\u001b[32m      3\u001b[39m print(\u001b[33m\"Average:\"\u001b[39m, average([\u001b[32m85\u001b[39m, \u001b[32m90\u001b[39m, \u001b[32m80\u001b[39m]))\n\u001b[32m      4\u001b[39m print(\u001b[33m\"Grade:\"\u001b[39m, grade(\u001b[32m85\u001b[39m))\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'school_tools'"
     ]
    }
   ],
   "source": [
    "# import the functions from the school_tools module\n",
    "from school_tools import average, grade, report\n",
    "\n",
    "print(\"Average:\", average([85, 90, 80]))\n",
    "print(\"Grade:\", grade(85))\n",
    "\n",
    "print(report(\"Ali\", [85, 90, 80]))\n",
    "print(report(\"Sara\", [70, 75, 80]))\n",
    "print(report(\"Ahmed\", [45, 55, 60]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78a2b235",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
