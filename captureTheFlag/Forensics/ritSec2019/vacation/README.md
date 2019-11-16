# Solve

### Steps

* This question has a hint `These are my favorite places to visit`

* Using the similar technique from the last challenge
```
srimbp-623:vacation sri$ file chromebin 
chromebin: POSIX tar archive (GNU)
srimbp-623:vacation sri$ tar tvf chromebin 
```

* First thought is to look at bookmarks but that does not help... Fail
  - to look at the `history database` --> looking at the visit_count in the urls table to correlate most visit count
```
srimbp-623:Default sri$ sqlite3 History
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite> .tables
downloads                meta                     urls                   
downloads_slices         segment_usage            visit_source           
downloads_url_chains     segments                 visits                 
keyword_search_terms     typed_url_sync_metadata
sqlite> select * from urls
   ...> ;
36|http://google.com/|Google|2|2|13218330672211254|0
37|http://www.google.com/|Google|2|0|13218330672211254|0
38|https://www.google.com/|Google|4|0|13218330672777218|0
...
...
...

sqlite> select * from visits;
1|36|13218330266705632|0|268435457|1|0|1
2|37|13218330266705632|1|-2147483647|0|0|0
3|38|13218330266705632|2|-1610612735|0|0|0
...
...
...

sqlite> .schema visits
CREATE TABLE visits(id INTEGER PRIMARY KEY,url INTEGER NOT NULL,visit_time INTEGER NOT NULL,from_visit INTEGER,transition INTEGER DEFAULT 0 NOT NULL,segment_id INTEGER,visit_duration INTEGER DEFAULT 0 NOT NULL,incremented_omnibox_typed_score BOOLEAN DEFAULT FALSE NOT NULL);
CREATE INDEX visits_url_index ON visits (url);
CREATE INDEX visits_from_index ON visits (from_visit);
CREATE INDEX visits_time_index ON visits (visit_time);


sqlite> .schema visit_source
CREATE TABLE visit_source(id INTEGER PRIMARY KEY,source INTEGER NOT NULL);
sqlite> .schema urls
CREATE TABLE urls(id INTEGER PRIMARY KEY AUTOINCREMENT,url LONGVARCHAR,title LONGVARCHAR,visit_count INTEGER DEFAULT 0 NOT NULL,typed_count INTEGER DEFAULT 0 NOT NULL,last_visit_time INTEGER NOT NULL,hidden INTEGER DEFAULT 0 NOT NULL);
CREATE INDEX urls_url_index ON urls (url);

sqlite> .schema urls
CREATE TABLE urls(id INTEGER PRIMARY KEY AUTOINCREMENT,url LONGVARCHAR,title LONGVARCHAR,visit_count INTEGER DEFAULT 0 NOT NULL,typed_count INTEGER DEFAULT 0 NOT NULL,last_visit_time INTEGER NOT NULL,hidden INTEGER DEFAULT 0 NOT NULL);
CREATE INDEX urls_url_index ON urls (url);

sqlite> select url from urls where visit_count=(select max(visit_count) from urls);
https://www.google.com/
sqlite> select url, MAX(visit_count) from urls group by id;
```

* Second attempt to look at bookmarks --> checked all the urls 
```
srimbp-623:Default sri$ cat Bookmarks
{
   "checksum": "3ad95cd85bbbf13d3f95c97664a9d48f",
   "roots": {
      "bookmark_bar": {
         "children": [  ],
         "date_added": "13218332312969905",
         "date_modified": "13218332420496045",
         "guid": "00000000-0000-4000-A000-000000000002",
         "id": "1",
         "name": "Bookmarks bar",
         "type": "folder"
...
...
...
```

* Thought of looking into the top sites that occur as thumbnails in chrome --> TopSites DB
```
srimbp-623:Default sri$ sqlite3 Top\ Sites
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite> .tables
meta       top_sites
sqlite> select * from top_sites
   ...> ;
https://chrome.google.com/webstore?hl=en|1|Web Store|https://chrome.google.com/webstore?hl=en
http://google.com/|0|Google|http://www.google.com/ https://www.google.com/ http://google.com/
sqlite> 
```

