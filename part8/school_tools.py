{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "737d78d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Testing school tools\n",
      "80.0\n",
      "A\n",
      "Ali: Average = 85.00, Grade = A\n"
     ]
    }
   ],
   "source": [
    "\n",
    "def average(marks):\n",
    "    return sum(marks) / len(marks)\n",
    "\n",
    "\n",
    "def grade(avg):\n",
    "    if avg >= 80:\n",
    "        return \"A\"\n",
    "    elif avg >= 70:\n",
    "        return \"B\"\n",
    "    elif avg >= 60:\n",
    "        return \"C\"\n",
    "    elif avg >= 33:\n",
    "        return \"D\"\n",
    "    else:\n",
    "        return \"Fail\"\n",
    "\n",
    "\n",
    "def report(name, marks):\n",
    "    avg = average(marks)\n",
    "    student_grade = grade(avg)\n",
    "    return f\"{name}: Average = {avg:.2f}, Grade = {student_grade}\"\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    print(\"Testing school tools\")\n",
    "\n",
    "    print(average([80, 90, 70]))\n",
    "    print(grade(80))\n",
    "    print(report(\"Ali\", [85, 90, 80]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b2a48f6",
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
