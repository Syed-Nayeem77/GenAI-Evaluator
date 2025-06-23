{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3fbc6ccb-159f-485a-88fb-2b680960b0d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estimated cost: 0.002\n"
     ]
    }
   ],
   "source": [
    "def calculate_cost(prompt_tokens, completion_tokens):\n",
    "    COST_PER_1K = 0.002  # Adjust based on model\n",
    "    total_tokens = prompt_tokens + completion_tokens\n",
    "    return (total_tokens / 1000) * COST_PER_1K\n",
    "\n",
    "# Example\n",
    "print(\"Estimated cost:\", calculate_cost(300, 700))  # Should output $0.002\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7f232e3e-bed1-4c78-a7b9-a2fab165a7a6",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3576482752.py, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[4], line 5\u001b[1;36m\u001b[0m\n\u001b[1;33m    > Sample evaluation on 2 generated summaries:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "## 🎥 Demo\n",
    "\n",
    "![Demo](demo.gif)\n",
    "\n",
    "> Sample evaluation on 2 generated summaries:\n",
    "> ```\n",
    "> References: [\"The sky is blue\", \"It is raining\"]\n",
    "> Predictions: [\"The sky was blue\", \"It rains\"]\n",
    "> ```\n",
    "\n",
    "Output:\n",
    "- BLEU: 0.0\n",
    "- BERTScore F1: 0.94\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e59f147a-62ee-4585-8f95-f33a056b02cc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
