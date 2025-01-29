{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b737cec6",
   "metadata": {
    "_cell_guid": "03e8de12-9585-4b81-a83e-763257180cf2",
    "_uuid": "a71c70ed-04d6-41cf-a224-afe831d1b176",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2025-01-29T21:00:07.376023Z",
     "iopub.status.busy": "2025-01-29T21:00:07.375492Z",
     "iopub.status.idle": "2025-01-29T21:00:15.665139Z",
     "shell.execute_reply": "2025-01-29T21:00:15.663791Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 8.296184,
     "end_time": "2025-01-29T21:00:15.666857",
     "exception": false,
     "start_time": "2025-01-29T21:00:07.370673",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting symspellpy\r\n",
      "  Downloading symspellpy-6.7.8-py3-none-any.whl.metadata (3.9 kB)\r\n",
      "Collecting editdistpy>=0.1.3 (from symspellpy)\r\n",
      "  Downloading editdistpy-0.1.5-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.9 kB)\r\n",
      "Downloading symspellpy-6.7.8-py3-none-any.whl (2.6 MB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.6/2.6 MB\u001b[0m \u001b[31m34.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading editdistpy-0.1.5-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (144 kB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m144.1/144.1 kB\u001b[0m \u001b[31m6.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hInstalling collected packages: editdistpy, symspellpy\r\n",
      "Successfully installed editdistpy-0.1.5 symspellpy-6.7.8\r\n",
      "/kaggle/input/frequency-dictionary-en-82-765/frequency_dictionary_en_82_765.txt\n",
      "/kaggle/input/wow-classic-gamer-jargon-and-terms-dataset/wow_comments.csv\n",
      "                                          videoTitle        channelName  \\\n",
      "0   WoW Classic - Assault on Blackwing Lair Now Live  World of Warcraft   \n",
      "1  Call of the Crusade – Champions Trailer| Wrath...  World of Warcraft   \n",
      "2                                A Toast to 15 Years  World of Warcraft   \n",
      "3     A New Dawn | Mythic Dungeon International 2024  World of Warcraft   \n",
      "4  WoW® Classic with Creators Episode 6: Tom Chilton  World of Warcraft   \n",
      "\n",
      "                    commentId                 channelId      videoId  \\\n",
      "0  UgzsF4n3XkKyD8glmaR4AaABAg  UCbLj9QP9FAaHs_647QckGtg  l7ivDtWjzQg   \n",
      "1  UgyKDCeJQqRSl0QFihx4AaABAg  UCbLj9QP9FAaHs_647QckGtg  j0OuFcb2Hqo   \n",
      "2  UgyqmEErPE4W4lryM1B4AaABAg  UCbLj9QP9FAaHs_647QckGtg  iCn14KLCerY   \n",
      "3  UgwzzxSaUiD_qdC5MCF4AaABAg  UCbLj9QP9FAaHs_647QckGtg  tn9LKwAaQjc   \n",
      "4  Ugw5YljDwo-9I4pqJMx4AaABAg  UCbLj9QP9FAaHs_647QckGtg  ii2255XpJ-s   \n",
      "\n",
      "                                       textOriginal  likeCount  \\\n",
      "0  ! ! ! F I  X   W A Y C R E S T   M A N O R ! ! !          0   \n",
      "1                     ! ! ! H U R R I C A N E ! ! !          0   \n",
      "2                        !! BARD CLASS CONFIRMED !!          0   \n",
      "3                                 !!! MANDATORY !!!          0   \n",
      "4           !!! STOP REMOVING NEGATIVE COMMENTS !!!          1   \n",
      "\n",
      "            publishedAt  \n",
      "0  2020-04-07T18:19:48Z  \n",
      "1  2023-10-15T05:45:46Z  \n",
      "2  2019-08-28T13:34:33Z  \n",
      "3  2024-02-14T17:15:00Z  \n",
      "4  2019-10-11T13:03:38Z  \n"
     ]
    }
   ],
   "source": [
    "!pip install symspellpy\n",
    "import re\n",
    "import pandas as pd\n",
    "from collections import Counter\n",
    "from tqdm import tqdm\n",
    "from symspellpy import SymSpell, Verbosity  # <-- Import SymSpell here\n",
    "\n",
    "\n",
    "# List available files\n",
    "import os\n",
    "for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "    for filename in filenames:\n",
    "        print(os.path.join(dirname, filename))\n",
    "\n",
    "# Load the dataset\n",
    "file_path = '/kaggle/input/wow-classic-gamer-jargon-and-terms-dataset/wow_comments.csv'\n",
    "df = pd.read_csv(file_path, sep=',')\n",
    "print(df.head())\n",
    "\n",
    "tqdm.pandas()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2317dd0e",
   "metadata": {
    "papermill": {
     "duration": 0.002758,
     "end_time": "2025-01-29T21:00:15.673108",
     "exception": false,
     "start_time": "2025-01-29T21:00:15.670350",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Above are the libraries being used in the project, and the code for loading the dataset and reading it. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "243269ac",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-01-29T21:00:15.680330Z",
     "iopub.status.busy": "2025-01-29T21:00:15.679930Z",
     "iopub.status.idle": "2025-01-29T21:01:02.314525Z",
     "shell.execute_reply": "2025-01-29T21:01:02.313238Z"
    },
    "papermill": {
     "duration": 46.640202,
     "end_time": "2025-01-29T21:01:02.316230",
     "exception": false,
     "start_time": "2025-01-29T21:00:15.676028",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Frequency dictionary loaded successfully.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Generating bigrams: 100%|██████████| 108088/108088 [00:01<00:00, 65823.85it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bigram dictionary generated and saved to generated_bigram_dictionary.txt.\n",
      "Bigram dictionary loaded successfully.\n",
      "WoW-specific terms added successfully.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████| 108088/108088 [00:39<00:00, 2702.65it/s]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bigram-based corrections and cleaning completed. Results saved to 'cleaned_comments_final.csv'.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "from collections import Counter\n",
    "from symspellpy import SymSpell\n",
    "import re\n",
    "from tqdm import tqdm\n",
    "\n",
    "# Define the path to the Kaggle dataset\n",
    "frequency_dictionary_dir = '/kaggle/input/frequency-dictionary-en-82-765'\n",
    "frequency_dictionary_path = os.path.join(frequency_dictionary_dir, \"frequency_dictionary_en_82_765.txt\")\n",
    "\n",
    "# Initialize SymSpell\n",
    "sym_spell = SymSpell(max_dictionary_edit_distance=2)\n",
    "\n",
    "# Load the frequency dictionary\n",
    "sym_spell.load_dictionary(frequency_dictionary_path, term_index=0, count_index=1)\n",
    "print(\"Frequency dictionary loaded successfully.\")\n",
    "\n",
    "# Generate the bigram dictionary from the dataset\n",
    "def generate_bigrams(text):\n",
    "    \"\"\"\n",
    "    Generate bigrams from a given text.\n",
    "    \"\"\"\n",
    "    # Extract words (alphanumeric only) and convert to lowercase\n",
    "    words = re.findall(r'\\b\\w+\\b', text.lower())\n",
    "    # Create bigram pairs\n",
    "    return zip(words, words[1:])\n",
    "\n",
    "# Count bigram frequencies\n",
    "bigrams = Counter()\n",
    "tqdm.pandas()  # Enable progress bar for large datasets\n",
    "\n",
    "# Assuming df['textOriginal'] contains the raw comments\n",
    "for comment in tqdm(df['textOriginal'], desc=\"Generating bigrams\"):\n",
    "    bigrams.update(generate_bigrams(comment))\n",
    "\n",
    "# Save the bigram dictionary to a file\n",
    "bigram_file = \"generated_bigram_dictionary.txt\"\n",
    "with open(bigram_file, \"w\") as file:\n",
    "    for bigram, freq in bigrams.most_common():\n",
    "        file.write(f\"{' '.join(bigram)}\\t{freq}\\n\")\n",
    "\n",
    "print(f\"Bigram dictionary generated and saved to {bigram_file}.\")\n",
    "\n",
    "# Step 4: Load the bigram dictionary into SymSpell\n",
    "sym_spell.load_bigram_dictionary(bigram_file, term_index=0, count_index=1)\n",
    "print(\"Bigram dictionary loaded successfully.\")\n",
    "\n",
    "# Step 5: Add domain-specific terms (World of Warcraft terms)\n",
    "wow_terms = [\n",
    "    \"Dalaran\", \"Sylvanas\", \"Arthas\", \"Blizzard\", \"Horde\", \"Alliance\", \"Shadowlands\",\n",
    "    \"Dragonflight\", \"Wrath\", \"Warcraft\", \"Illidan\", \"Thrall\", \"Jaina\",\n",
    "    \"Anduin\", \"Bolvar\", \"tank\", \"healer\", \"dps\", \"raid\", \"mythic\", \"dungeon\",\n",
    "    \"Stormwind\", \"Icecrown\", \"loot\", \"tier\", \"gear\", \"dot\", \"aoe\", \"waycrest\", \"Argus\"\n",
    "]\n",
    "\n",
    "for term in wow_terms:\n",
    "    sym_spell.create_dictionary_entry(term.lower(), 1)\n",
    "print(\"WoW-specific terms added successfully.\")\n",
    "\n",
    "from symspellpy import SymSpell, Verbosity\n",
    "\n",
    "# Define the correction function\n",
    "def correct_with_symspell(text):\n",
    "    \"\"\"\n",
    "    Corrects spelling mistakes in the text using SymSpell.\n",
    "    \"\"\"\n",
    "    words = text.split()  # Split the text into words\n",
    "    corrected_words = []\n",
    "\n",
    "    for word in words:\n",
    "        # Keep WoW terms intact\n",
    "        if word.lower() in wow_terms:\n",
    "            corrected_words.append(word)\n",
    "        else:\n",
    "            # Use SymSpell for correction\n",
    "            suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)\n",
    "            corrected_words.append(suggestions[0].term if suggestions else word)\n",
    "\n",
    "    return \" \".join(corrected_words)\n",
    "\n",
    "# Apply the spell correction pipeline\n",
    "df['cleanedComments'] = df['textOriginal'].progress_apply(correct_with_symspell)\n",
    "\n",
    "# Save the cleaned data\n",
    "df[['textOriginal', 'cleanedComments']].to_csv(\"cleaned_comments_final.csv\", index=False)\n",
    "print(\"Bigram-based corrections and cleaning completed. Results saved to 'cleaned_comments_final.csv'.\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b4dd5755",
   "metadata": {
    "papermill": {
     "duration": 0.022294,
     "end_time": "2025-01-29T21:01:02.361738",
     "exception": false,
     "start_time": "2025-01-29T21:01:02.339444",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Here we are going to initialize SymSpell and create a domain-specific dictionary that will house words that are specific to World of Warcraft, and gaming jargon. \n",
    "\n",
    "Additionally - we are running a word frequencey script to determine what words are showing up the most in the dataset, so that we are only including relevant words into this dataframe. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "50d10ac3",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-01-29T21:01:02.414612Z",
     "iopub.status.busy": "2025-01-29T21:01:02.414272Z",
     "iopub.status.idle": "2025-01-29T21:01:28.426780Z",
     "shell.execute_reply": "2025-01-29T21:01:28.425654Z"
    },
    "papermill": {
     "duration": 26.038883,
     "end_time": "2025-01-29T21:01:28.429011",
     "exception": false,
     "start_time": "2025-01-29T21:01:02.390128",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "100%|██████████| 108088/108088 [00:01<00:00, 103454.45it/s]\n",
      "100%|██████████| 108088/108088 [00:00<00:00, 236003.96it/s]\n",
      "100%|██████████| 108088/108088 [00:00<00:00, 168942.73it/s]\n",
      "100%|██████████| 108088/108088 [00:23<00:00, 4536.12it/s]"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Text cleaning pipeline applied successfully.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "from collections import Counter\n",
    "from symspellpy import SymSpell, Verbosity\n",
    "from tqdm import tqdm\n",
    "\n",
    "# Updated cleaning function as of 1/28/2025 @ 1:23pm\n",
    "def clean_text(text):\n",
    "    text = text.lower().strip()  # Convert to lowercase and remove leading and trailing spaces.\n",
    "    text = re.sub(r'[^a-zA-Z0-9\\s-]', '', text)  # Remove unnecessary symbols but keep spaces and hyphens.\n",
    "    text = re.sub(r'\\s+', ' ', text)  # Normalize whitespace to a single space.\n",
    "    return text\n",
    "\n",
    "def remove_emoji(text):\n",
    "    emoji_pattern = re.compile(\"[\"\n",
    "                               u\"\\U0001F600-\\U0001F64F\"\n",
    "                               u\"\\U0001F300-\\U0001F5FF\"\n",
    "                               u\"\\U0001F680-\\U0001F6FF\"\n",
    "                               u\"\\U0001F1E0-\\U0001F1FF\"\n",
    "                               u\"\\U00002702-\\U000027B0\"\n",
    "                               u\"\\U000024C2-\\U0001F251\"\n",
    "                               \"]+\", flags=re.UNICODE)\n",
    "    return emoji_pattern.sub(r'', text)\n",
    "\n",
    "# Updated spacing fix to avoid word merging.\n",
    "def fix_spacing(text):\n",
    "    # Ensure at least one space between words.\n",
    "    return re.sub(r'(\\w)([A-Z])', r'\\1 \\2', text)  # Splits incorrectly merged words.\n",
    "\n",
    "# Updated spell correction to preserve WoW Terms as of 1/28/2025 @ 1:32pm \n",
    "def correct_with_symspell(text):  \n",
    "    words = text.split()  # Split input text into a list of individual words\n",
    "    corrected_words = []  # Container for corrected words\n",
    "\n",
    "    for word in words:  # Loop through each word in the list\n",
    "        if word.lower() in wow_terms:  # Check if the word exists in the WoW terms set\n",
    "            corrected_words.append(word)  # Keep WoW terms unchanged\n",
    "        else:\n",
    "            suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)  \n",
    "            corrected_words.append(suggestions[0].term if suggestions else word)  # Use correction if available, otherwise keep the word\n",
    "\n",
    "    return \" \".join(corrected_words)  # Join words back into a cleaned sentence\n",
    "\n",
    "# Apply the cleaning pipeline\n",
    "df['newComments'] = df['textOriginal'].progress_apply(clean_text)  # Apply basic cleaning\n",
    "df['newComments'] = df['newComments'].progress_apply(remove_emoji)  # Remove emojis\n",
    "df['newComments'] = df['newComments'].progress_apply(fix_spacing)  # Fix spacing issues\n",
    "df['newComments'] = df['newComments'].progress_apply(correct_with_symspell)  # Apply spell correction\n",
    "\n",
    "print(\"Text cleaning pipeline applied successfully.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "94b1f135",
   "metadata": {
    "papermill": {
     "duration": 0.034984,
     "end_time": "2025-01-29T21:01:28.500202",
     "exception": false,
     "start_time": "2025-01-29T21:01:28.465218",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Above is additional cleaning code functions that do the following things: (Covert lowercase, remove spaces between letters, remove non-alphanumeric characters, normalize whitespace, remove emojis, and remove single characters with spaces.)\n",
    "\n",
    "Note the change being made to ensure spaces between words is being made here, the issue causing this is this line of code  **text = re.sub(r'(?<=\\w)\\s(?=\\w)', '', text)** "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45c31d36",
   "metadata": {
    "papermill": {
     "duration": 0.034557,
     "end_time": "2025-01-29T21:01:28.569387",
     "exception": false,
     "start_time": "2025-01-29T21:01:28.534830",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 4235459,
     "sourceId": 10447351,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 6564282,
     "sourceId": 10604356,
     "sourceType": "datasetVersion"
    }
   ],
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
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
   "version": "3.10.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 84.893975,
   "end_time": "2025-01-29T21:01:29.525001",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-01-29T21:00:04.631026",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
