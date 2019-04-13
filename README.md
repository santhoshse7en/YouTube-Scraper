# YouTube-Scraper

This python script scrape the YouTube details as follows like

    * Channel Name
    * Subscribers Count
    * Published Date
    * Views
    * Likes
    * Dislikes
    
and finally, returns the output in dictionary format

## Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following
```bash
pip install beautifulsoup4
pip install requests
pip install argparse
```
## Usage

Download it by clicking the green download button here on Github. You only need to parse argument of YouTube URL.
```bash
python main.py -youtube_url https://www.youtube.com/watch?v=IRbuo1bwOoc

or

python main.py -yt https://www.youtube.com/watch?v=IRbuo1bwOoc
```

## Output

![capture](https://user-images.githubusercontent.com/47944792/53887560-8f72d000-4048-11e9-9875-6aa58589c2ab.PNG)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
