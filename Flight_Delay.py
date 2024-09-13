{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOLkswRmCa0WisYYjoQ3EwC",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bhoomikark/Student_management_System/blob/main/Flight_Delay.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "id": "DWZ_zCKB4lk3",
        "outputId": "dbdce90f-be88-4fa7-f6bc-b441d056c681"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "[Errno 2] No such file or directory: '2018 (1).csv'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-be62a183c4ab>\u001b[0m in \u001b[0;36m<cell line: 5>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# Step 2: Load the dataset into a Pandas DataFrame (replace '2018 (1).csv' with the actual filename if different)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'2018 (1).csv'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;31m# Step 3: Preview the dataset\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36mread_csv\u001b[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[0m\n\u001b[1;32m    946\u001b[0m     \u001b[0mkwds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkwds_defaults\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    947\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 948\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    949\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    950\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_read\u001b[0;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[1;32m    609\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    610\u001b[0m     \u001b[0;31m# Create the parser.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 611\u001b[0;31m     \u001b[0mparser\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    612\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    613\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[1;32m   1446\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1447\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhandles\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mIOHandles\u001b[0m \u001b[0;34m|\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1448\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1449\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1450\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[0;34m(self, f, engine)\u001b[0m\n\u001b[1;32m   1703\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0;34m\"b\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mmode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1704\u001b[0m                     \u001b[0mmode\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;34m\"b\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1705\u001b[0;31m             self.handles = get_handle(\n\u001b[0m\u001b[1;32m   1706\u001b[0m                 \u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1707\u001b[0m                 \u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/common.py\u001b[0m in \u001b[0;36mget_handle\u001b[0;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[1;32m    861\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mencoding\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0;34m\"b\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    862\u001b[0m             \u001b[0;31m# Encoding\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 863\u001b[0;31m             handle = open(\n\u001b[0m\u001b[1;32m    864\u001b[0m                 \u001b[0mhandle\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    865\u001b[0m                 \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '2018 (1).csv'"
          ]
        }
      ],
      "source": [
        "from google.colab import files\n",
        "import pandas as pd\n",
        "\n",
        "# Step 2: Load the dataset into a Pandas DataFrame (replace '2018 (1).csv' with the actual filename if different)\n",
        "df = pd.read_csv('2018 (1).csv')\n",
        "\n",
        "# Step 3: Preview the dataset\n",
        "print(df.head())\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "import pandas as pd\n",
        "\n",
        "\n",
        "# Step 2: Load the dataset into a Pandas DataFrame (replace '2018 (1).csv' with the actual filename if different)\n",
        "df = pd.read_csv('2018 (1).csv')\n",
        "\n",
        "# Step 3: Preview the dataset\n",
        "print(df.head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 391
        },
        "id": "Mo3pfm8y5wQs",
        "outputId": "60c6ca3f-4886-42d0-d48e-a3fb837b7715"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "[Errno 2] No such file or directory: '2018 (1).csv'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-ebb57db94ccd>\u001b[0m in \u001b[0;36m<cell line: 6>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# Step 2: Load the dataset into a Pandas DataFrame (replace '2018 (1).csv' with the actual filename if different)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'2018 (1).csv'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;31m# Step 3: Preview the dataset\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36mread_csv\u001b[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[0m\n\u001b[1;32m    946\u001b[0m     \u001b[0mkwds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkwds_defaults\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    947\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 948\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    949\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    950\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_read\u001b[0;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[1;32m    609\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    610\u001b[0m     \u001b[0;31m# Create the parser.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 611\u001b[0;31m     \u001b[0mparser\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTextFileReader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    612\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    613\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mchunksize\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0miterator\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[1;32m   1446\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1447\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhandles\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mIOHandles\u001b[0m \u001b[0;34m|\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1448\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_make_engine\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1449\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1450\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/parsers/readers.py\u001b[0m in \u001b[0;36m_make_engine\u001b[0;34m(self, f, engine)\u001b[0m\n\u001b[1;32m   1703\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0;34m\"b\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mmode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1704\u001b[0m                     \u001b[0mmode\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;34m\"b\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1705\u001b[0;31m             self.handles = get_handle(\n\u001b[0m\u001b[1;32m   1706\u001b[0m                 \u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1707\u001b[0m                 \u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/io/common.py\u001b[0m in \u001b[0;36mget_handle\u001b[0;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[1;32m    861\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mencoding\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0;34m\"b\"\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    862\u001b[0m             \u001b[0;31m# Encoding\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 863\u001b[0;31m             handle = open(\n\u001b[0m\u001b[1;32m    864\u001b[0m                 \u001b[0mhandle\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    865\u001b[0m                 \u001b[0mioargs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '2018 (1).csv'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "import pandas as pd\n",
        "\n",
        "# Step 1: Upload the file\n",
        "uploaded = files.upload()\n",
        "\n",
        "# Step 2: Load the dataset into a Pandas DataFrame (replace '2018 (1).csv' with the actual filename if different)\n",
        "df = pd.read_csv('2018 (1).csv')\n",
        "\n",
        "# Step 3: Preview the dataset\n",
        "print(df.head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 576
        },
        "id": "9b_RRsNP56ZG",
        "outputId": "bc8f2a8b-3d44-4dae-87c0-223e1b1dc4c6"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-2e2683fe-50e3-4f19-9eb9-8fd02a527a91\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-2e2683fe-50e3-4f19-9eb9-8fd02a527a91\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving 2018 (1).csv to 2018 (1).csv\n",
            "      FL_DATE OP_CARRIER  OP_CARRIER_FL_NUM ORIGIN DEST  CRS_DEP_TIME  \\\n",
            "0  2018-01-01         UA               2429    EWR  DEN          1517   \n",
            "1  2018-01-01         UA               2427    LAS  SFO          1115   \n",
            "2  2018-01-01         UA               2426    SNA  DEN          1335   \n",
            "3  2018-01-01         UA               2425    RSW  ORD          1546   \n",
            "4  2018-01-01         UA               2424    ORD  ALB           630   \n",
            "\n",
            "   DEP_TIME  DEP_DELAY  TAXI_OUT  WHEELS_OFF  ...  CRS_ELAPSED_TIME  \\\n",
            "0    1512.0       -5.0      15.0      1527.0  ...             268.0   \n",
            "1    1107.0       -8.0      11.0      1118.0  ...              99.0   \n",
            "2    1330.0       -5.0      15.0      1345.0  ...             134.0   \n",
            "3    1552.0        6.0      19.0      1611.0  ...             190.0   \n",
            "4     650.0       20.0      13.0       703.0  ...             112.0   \n",
            "\n",
            "   ACTUAL_ELAPSED_TIME  AIR_TIME  DISTANCE  CARRIER_DELAY  WEATHER_DELAY  \\\n",
            "0                250.0     225.0    1605.0            NaN            NaN   \n",
            "1                 83.0      65.0     414.0            NaN            NaN   \n",
            "2                126.0     106.0     846.0            NaN            NaN   \n",
            "3                182.0     157.0    1120.0            NaN            NaN   \n",
            "4                106.0      83.0     723.0            NaN            NaN   \n",
            "\n",
            "  NAS_DELAY  SECURITY_DELAY  LATE_AIRCRAFT_DELAY  Unnamed: 27  \n",
            "0       NaN             NaN                  NaN          NaN  \n",
            "1       NaN             NaN                  NaN          NaN  \n",
            "2       NaN             NaN                  NaN          NaN  \n",
            "3       NaN             NaN                  NaN          NaN  \n",
            "4       NaN             NaN                  NaN          NaN  \n",
            "\n",
            "[5 rows x 28 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Step 4: Check for missing values\n",
        "print(\"Missing values per column:\")\n",
        "print(df.isnull().sum())\n",
        "\n",
        "# Step 5: Fill missing values with column mean or drop rows\n",
        "# You can use df.dropna() to remove rows with missing data, but here we will fill missing values with the mean\n",
        "df.fillna(df.mean(), inplace=True)\n",
        "\n",
        "# Step 6: Verify that missing values are handled\n",
        "print(\"Missing values after filling:\")\n",
        "print(df.isnull().sum())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 911
        },
        "id": "FBt8XcF88hBt",
        "outputId": "a62da3b7-14f2-4fbc-87df-a2b165374fea"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Missing values per column:\n",
            "FL_DATE                     0\n",
            "OP_CARRIER                  0\n",
            "OP_CARRIER_FL_NUM           0\n",
            "ORIGIN                      0\n",
            "DEST                        0\n",
            "CRS_DEP_TIME                0\n",
            "DEP_TIME                11547\n",
            "DEP_DELAY               11858\n",
            "TAXI_OUT                11692\n",
            "WHEELS_OFF              11692\n",
            "WHEELS_ON               12012\n",
            "TAXI_IN                 12012\n",
            "CRS_ARR_TIME                0\n",
            "ARR_TIME                12012\n",
            "ARR_DELAY               12713\n",
            "CANCELLED                   0\n",
            "CANCELLATION_CODE      277728\n",
            "DIVERTED                    0\n",
            "CRS_ELAPSED_TIME            0\n",
            "ACTUAL_ELAPSED_TIME     12600\n",
            "AIR_TIME                12601\n",
            "DISTANCE                    1\n",
            "CARRIER_DELAY          227186\n",
            "WEATHER_DELAY          227186\n",
            "NAS_DELAY              227186\n",
            "SECURITY_DELAY         227186\n",
            "LATE_AIRCRAFT_DELAY    227186\n",
            "Unnamed: 27            289496\n",
            "dtype: int64\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "unsupported operand type(s) for +: 'int' and 'str'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-1c70168d1314>\u001b[0m in \u001b[0;36m<cell line: 7>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# Step 5: Fill missing values with column mean or drop rows\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;31m# You can use df.dropna() to remove rows with missing data, but here we will fill missing values with the mean\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfillna\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minplace\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      8\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;31m# Step 6: Verify that missing values are handled\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36mmean\u001b[0;34m(self, axis, skipna, numeric_only, **kwargs)\u001b[0m\n\u001b[1;32m  11333\u001b[0m         \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11334\u001b[0m     ):\n\u001b[0;32m> 11335\u001b[0;31m         \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmean\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnumeric_only\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m  11336\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresult\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mSeries\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11337\u001b[0m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__finalize__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"mean\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36mmean\u001b[0;34m(self, axis, skipna, numeric_only, **kwargs)\u001b[0m\n\u001b[1;32m  11990\u001b[0m         \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11991\u001b[0m     ) -> Series | float:\n\u001b[0;32m> 11992\u001b[0;31m         return self._stat_function(\n\u001b[0m\u001b[1;32m  11993\u001b[0m             \u001b[0;34m\"mean\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnanops\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnanmean\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnumeric_only\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11994\u001b[0m         )\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36m_stat_function\u001b[0;34m(self, name, func, axis, skipna, numeric_only, **kwargs)\u001b[0m\n\u001b[1;32m  11947\u001b[0m         \u001b[0mvalidate_bool_kwarg\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mskipna\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"skipna\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnone_allowed\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11948\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m> 11949\u001b[0;31m         return self._reduce(\n\u001b[0m\u001b[1;32m  11950\u001b[0m             \u001b[0mfunc\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mskipna\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnumeric_only\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnumeric_only\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11951\u001b[0m         )\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36m_reduce\u001b[0;34m(self, op, name, axis, skipna, numeric_only, filter_type, **kwds)\u001b[0m\n\u001b[1;32m  11202\u001b[0m         \u001b[0;31m# After possibly _get_data and transposing, we are now in the\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11203\u001b[0m         \u001b[0;31m#  simple case where we can use BlockManager.reduce\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m> 11204\u001b[0;31m         \u001b[0mres\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_mgr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreduce\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mblk_func\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m  11205\u001b[0m         \u001b[0mout\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_constructor_from_mgr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mres\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxes\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mres\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0maxes\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11206\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mout_dtype\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mout\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdtype\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;34m\"boolean\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/internals/managers.py\u001b[0m in \u001b[0;36mreduce\u001b[0;34m(self, func)\u001b[0m\n\u001b[1;32m   1457\u001b[0m         \u001b[0mres_blocks\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mlist\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mBlock\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1458\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0mblk\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mblocks\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1459\u001b[0;31m             \u001b[0mnbs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mblk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreduce\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfunc\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1460\u001b[0m             \u001b[0mres_blocks\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mextend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnbs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1461\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/internals/blocks.py\u001b[0m in \u001b[0;36mreduce\u001b[0;34m(self, func)\u001b[0m\n\u001b[1;32m    375\u001b[0m         \u001b[0;32massert\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mndim\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    376\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 377\u001b[0;31m         \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    378\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    379\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mndim\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36mblk_func\u001b[0;34m(values, axis)\u001b[0m\n\u001b[1;32m  11134\u001b[0m                     \u001b[0;32mreturn\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0marray\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mresult\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11135\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m> 11136\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mskipna\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m  11137\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m  11138\u001b[0m         \u001b[0;32mdef\u001b[0m \u001b[0m_get_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mDataFrame\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/nanops.py\u001b[0m in \u001b[0;36mf\u001b[0;34m(values, axis, skipna, **kwds)\u001b[0m\n\u001b[1;32m    145\u001b[0m                     \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0malt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mskipna\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    146\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 147\u001b[0;31m                 \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0malt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mskipna\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    148\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    149\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/nanops.py\u001b[0m in \u001b[0;36mnew_func\u001b[0;34m(values, axis, skipna, mask, **kwargs)\u001b[0m\n\u001b[1;32m    402\u001b[0m             \u001b[0mmask\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0misna\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    403\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 404\u001b[0;31m         \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mskipna\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mskipna\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmask\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmask\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    405\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    406\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mdatetimelike\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/nanops.py\u001b[0m in \u001b[0;36mnanmean\u001b[0;34m(values, axis, skipna, mask)\u001b[0m\n\u001b[1;32m    717\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    718\u001b[0m     \u001b[0mcount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_get_counts\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmask\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdtype\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdtype_count\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 719\u001b[0;31m     \u001b[0mthe_sum\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalues\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msum\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdtype\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdtype_sum\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    720\u001b[0m     \u001b[0mthe_sum\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_ensure_numeric\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mthe_sum\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    721\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/numpy/core/_methods.py\u001b[0m in \u001b[0;36m_sum\u001b[0;34m(a, axis, dtype, out, keepdims, initial, where)\u001b[0m\n\u001b[1;32m     47\u001b[0m def _sum(a, axis=None, dtype=None, out=None, keepdims=False,\n\u001b[1;32m     48\u001b[0m          initial=_NoValue, where=True):\n\u001b[0;32m---> 49\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mumr_sum\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdtype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mout\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkeepdims\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minitial\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwhere\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     50\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     51\u001b[0m def _prod(a, axis=None, dtype=None, out=None, keepdims=False,\n",
            "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for +: 'int' and 'str'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Step 4: Check for missing values\n",
        "print(\"Missing values per column:\")\n",
        "print(df.isnull().sum())\n",
        "\n",
        "# Step 5: Fill missing values for only numeric columns\n",
        "# Select only numeric columns and fill their missing values with the mean\n",
        "numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns\n",
        "df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())\n",
        "\n",
        "# Step 6: Verify that missing values are handled for numeric columns\n",
        "print(\"Missing values after filling (numeric columns):\")\n",
        "print(df[numeric_cols].isnull().sum())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2ZKKZsnp9T-A",
        "outputId": "3e67a5f4-522f-49b7-a73d-6a70b7e9811b"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Missing values per column:\n",
            "FL_DATE                     0\n",
            "OP_CARRIER                  0\n",
            "OP_CARRIER_FL_NUM           0\n",
            "ORIGIN                      0\n",
            "DEST                        0\n",
            "CRS_DEP_TIME                0\n",
            "DEP_TIME                11547\n",
            "DEP_DELAY               11858\n",
            "TAXI_OUT                11692\n",
            "WHEELS_OFF              11692\n",
            "WHEELS_ON               12012\n",
            "TAXI_IN                 12012\n",
            "CRS_ARR_TIME                0\n",
            "ARR_TIME                12012\n",
            "ARR_DELAY               12713\n",
            "CANCELLED                   0\n",
            "CANCELLATION_CODE      277728\n",
            "DIVERTED                    0\n",
            "CRS_ELAPSED_TIME            0\n",
            "ACTUAL_ELAPSED_TIME     12600\n",
            "AIR_TIME                12601\n",
            "DISTANCE                    1\n",
            "CARRIER_DELAY          227186\n",
            "WEATHER_DELAY          227186\n",
            "NAS_DELAY              227186\n",
            "SECURITY_DELAY         227186\n",
            "LATE_AIRCRAFT_DELAY    227186\n",
            "Unnamed: 27            289496\n",
            "dtype: int64\n",
            "Missing values after filling (numeric columns):\n",
            "OP_CARRIER_FL_NUM           0\n",
            "CRS_DEP_TIME                0\n",
            "DEP_TIME                    0\n",
            "DEP_DELAY                   0\n",
            "TAXI_OUT                    0\n",
            "WHEELS_OFF                  0\n",
            "WHEELS_ON                   0\n",
            "TAXI_IN                     0\n",
            "CRS_ARR_TIME                0\n",
            "ARR_TIME                    0\n",
            "ARR_DELAY                   0\n",
            "CANCELLED                   0\n",
            "DIVERTED                    0\n",
            "CRS_ELAPSED_TIME            0\n",
            "ACTUAL_ELAPSED_TIME         0\n",
            "AIR_TIME                    0\n",
            "DISTANCE                    0\n",
            "CARRIER_DELAY               0\n",
            "WEATHER_DELAY               0\n",
            "NAS_DELAY                   0\n",
            "SECURITY_DELAY              0\n",
            "LATE_AIRCRAFT_DELAY         0\n",
            "Unnamed: 27            289496\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "\n",
        "# Step 7: Identify categorical columns\n",
        "categorical_cols = df.select_dtypes(include=['object']).columns\n",
        "print(\"Categorical columns:\", categorical_cols)\n",
        "\n",
        "# Step 8: Apply Label Encoding for binary columns or One-Hot Encoding for others\n",
        "label_encoder = LabelEncoder()\n",
        "\n",
        "for col in categorical_cols:\n",
        "    if df[col].nunique() <= 2:  # For binary columns\n",
        "        df[col] = label_encoder.fit_transform(df[col])\n",
        "    else:  # For multi-class columns\n",
        "        df = pd.get_dummies(df, columns=[col], drop_first=True)\n",
        "\n",
        "# Step 9: Preview the dataset after encoding\n",
        "print(df.head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P_Q58EsN9hyW",
        "outputId": "0e348568-98ae-4d85-fcd3-251554941cfa"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Categorical columns: Index(['FL_DATE', 'OP_CARRIER', 'ORIGIN', 'DEST', 'CANCELLATION_CODE'], dtype='object')\n",
            "   OP_CARRIER_FL_NUM  CRS_DEP_TIME  DEP_TIME  DEP_DELAY  TAXI_OUT  WHEELS_OFF  \\\n",
            "0               2429          1517    1512.0       -5.0      15.0      1527.0   \n",
            "1               2427          1115    1107.0       -8.0      11.0      1118.0   \n",
            "2               2426          1335    1330.0       -5.0      15.0      1345.0   \n",
            "3               2425          1546    1552.0        6.0      19.0      1611.0   \n",
            "4               2424           630     650.0       20.0      13.0       703.0   \n",
            "\n",
            "   WHEELS_ON  TAXI_IN  CRS_ARR_TIME  ARR_TIME  ...  DEST_USA  DEST_VLD  \\\n",
            "0     1712.0     10.0          1745    1722.0  ...     False     False   \n",
            "1     1223.0      7.0          1254    1230.0  ...     False     False   \n",
            "2     1631.0      5.0          1649    1636.0  ...     False     False   \n",
            "3     1748.0      6.0          1756    1754.0  ...     False     False   \n",
            "4      926.0     10.0           922     936.0  ...     False     False   \n",
            "\n",
            "   DEST_VPS  DEST_WRG  DEST_XNA  DEST_YAK  DEST_YNG  DEST_YUM  \\\n",
            "0     False     False     False     False     False     False   \n",
            "1     False     False     False     False     False     False   \n",
            "2     False     False     False     False     False     False   \n",
            "3     False     False     False     False     False     False   \n",
            "4     False     False     False     False     False     False   \n",
            "\n",
            "   CANCELLATION_CODE_B  CANCELLATION_CODE_C  \n",
            "0                False                False  \n",
            "1                False                False  \n",
            "2                False                False  \n",
            "3                False                False  \n",
            "4                False                False  \n",
            "\n",
            "[5 rows x 721 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "# Step 10: Identify numeric columns\n",
        "numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns\n",
        "\n",
        "# Step 11: Apply StandardScaler to normalize the numeric columns\n",
        "scaler = StandardScaler()\n",
        "df[numerical_cols] = scaler.fit_transform(df[numerical_cols])\n",
        "\n",
        "# Step 12: Preview the scaled dataset\n",
        "print(df.head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ySGw-0y--CgE",
        "outputId": "ee4c0a49-d989-4f34-a265-22e583f9772c"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/utils/extmath.py:1050: RuntimeWarning: invalid value encountered in divide\n",
            "  updated_mean = (last_sum + new_sum) / updated_sample_count\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/utils/extmath.py:1055: RuntimeWarning: invalid value encountered in divide\n",
            "  T = new_sum / new_sample_count\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/utils/extmath.py:1075: RuntimeWarning: invalid value encountered in divide\n",
            "  new_unnormalized_variance -= correction**2 / new_sample_count\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   OP_CARRIER_FL_NUM  CRS_DEP_TIME  DEP_TIME  DEP_DELAY  TAXI_OUT  WHEELS_OFF  \\\n",
            "0          -0.091556      0.384718  0.351932  -0.371641 -0.282173    0.331283   \n",
            "1          -0.092606     -0.438026 -0.473134  -0.430096 -0.665899   -0.501571   \n",
            "2          -0.093131      0.012232 -0.018839  -0.371641 -0.282173   -0.039327   \n",
            "3          -0.093656      0.444070  0.433420  -0.157308  0.101553    0.502333   \n",
            "4          -0.094180     -1.430640 -1.404135   0.115479 -0.474036   -1.346643   \n",
            "\n",
            "   WHEELS_ON   TAXI_IN  CRS_ARR_TIME  ARR_TIME  ...  DEST_USA  DEST_VLD  \\\n",
            "0   0.461747  0.360632      0.490386  0.468645  ...     False     False   \n",
            "1  -0.485531 -0.119841     -0.463860 -0.475802  ...     False     False   \n",
            "2   0.304836 -0.440157      0.303813  0.303559  ...     False     False   \n",
            "3   0.531485 -0.279999      0.511765  0.530073  ...     False     False   \n",
            "4  -1.060871  0.360632     -1.109093 -1.040168  ...     False     False   \n",
            "\n",
            "   DEST_VPS  DEST_WRG  DEST_XNA  DEST_YAK  DEST_YNG  DEST_YUM  \\\n",
            "0     False     False     False     False     False     False   \n",
            "1     False     False     False     False     False     False   \n",
            "2     False     False     False     False     False     False   \n",
            "3     False     False     False     False     False     False   \n",
            "4     False     False     False     False     False     False   \n",
            "\n",
            "   CANCELLATION_CODE_B  CANCELLATION_CODE_C  \n",
            "0                False                False  \n",
            "1                False                False  \n",
            "2                False                False  \n",
            "3                False                False  \n",
            "4                False                False  \n",
            "\n",
            "[5 rows x 721 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "# Step 13: Define your target column (replace 'DelayStatus' with your actual target column name)\n",
        "target_column = 'DelayStatus'  # Modify this with your actual target\n",
        "\n",
        "# Step 14: Split the dataset into features (X) and target (y)\n",
        "X = df.drop(target_column, axis=1)\n",
        "y = df[target_column]\n",
        "\n",
        "# Step 15: Split the dataset into training and testing sets (80% train, 20% test)\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "\n",
        "# Step 16: Preview the shapes of the resulting datasets\n",
        "print(\"Training features shape:\", X_train.shape)\n",
        "print(\"Testing features shape:\", X_test.shape)\n",
        "print(\"Training labels shape:\", y_train.shape)\n",
        "print(\"Testing labels shape:\", y_test.shape)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 356
        },
        "id": "LYYr7BEI-LVN",
        "outputId": "5b3d85f2-fbc2-43ae-b389-96fac27f076f"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyError",
          "evalue": "\"['DelayStatus'] not found in axis\"",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-8-2930029b454b>\u001b[0m in \u001b[0;36m<cell line: 7>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;31m# Step 14: Split the dataset into features (X) and target (y)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m \u001b[0mX\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtarget_column\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      8\u001b[0m \u001b[0my\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mtarget_column\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36mdrop\u001b[0;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[1;32m   5342\u001b[0m                 \u001b[0mweight\u001b[0m  \u001b[0;36m1.0\u001b[0m     \u001b[0;36m0.8\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5343\u001b[0m         \"\"\"\n\u001b[0;32m-> 5344\u001b[0;31m         return super().drop(\n\u001b[0m\u001b[1;32m   5345\u001b[0m             \u001b[0mlabels\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlabels\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5346\u001b[0m             \u001b[0maxis\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36mdrop\u001b[0;34m(self, labels, axis, index, columns, level, inplace, errors)\u001b[0m\n\u001b[1;32m   4709\u001b[0m         \u001b[0;32mfor\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlabels\u001b[0m \u001b[0;32min\u001b[0m \u001b[0maxes\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mitems\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4710\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mlabels\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 4711\u001b[0;31m                 \u001b[0mobj\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_drop_axis\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlevel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   4712\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4713\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0minplace\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36m_drop_axis\u001b[0;34m(self, labels, axis, level, errors, only_slice)\u001b[0m\n\u001b[1;32m   4751\u001b[0m                 \u001b[0mnew_axis\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlevel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mlevel\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4752\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 4753\u001b[0;31m                 \u001b[0mnew_axis\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdrop\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabels\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merrors\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merrors\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   4754\u001b[0m             \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_indexer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnew_axis\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   4755\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mdrop\u001b[0;34m(self, labels, errors)\u001b[0m\n\u001b[1;32m   6998\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mmask\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0many\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   6999\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0merrors\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;34m\"ignore\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 7000\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"{labels[mask].tolist()} not found in axis\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   7001\u001b[0m             \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mindexer\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m~\u001b[0m\u001b[0mmask\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   7002\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdelete\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mindexer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyError\u001b[0m: \"['DelayStatus'] not found in axis\""
          ]
        }
      ]
    }
  ]
}