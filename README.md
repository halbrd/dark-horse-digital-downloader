For downloading comics at highest resolution from Dark Horse Digital.

Disclaimer: This is a really sketchy scraper and everything could totally break at any time.

Steps:

1. Open comic in web page

2. (Optional) Scroll through all the pages as fast as possible to preload them (results in more accurate auto-ordering), then refresh the page

3. Scroll through all pages, ideally stopping for at least 1 second on each page

4. Open Chrome Developer Tools with F12

5. Open Network tab

6. Right click on one of the rows, and select Copy > Copy all as HAR

7. Paste clipboard into input.json

8. Run script reasonably soon so that the session doesn't expire

9. Check the order of the output in /images - they should be in order as long as your internet connection is reasonable, but there could be some issues
