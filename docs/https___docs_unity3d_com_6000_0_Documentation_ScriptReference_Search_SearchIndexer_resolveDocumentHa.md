* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer-resolveDocumentHandler.html

#  [SearchIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html).resolveDocumentHandler
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
resolveDocumentHandler; 
### Description
Handler used to resolve a document ID to some other data string.
```
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

/// <summary>
/// Since the search indexes only contain string document IDs that must be unique,
/// you can use `resolveDocumentHandler` to transform these document IDs into something
/// that can be searched while running queries that contain simple words.
/// </summary>
static class Example_SearchIndexer_resolveDocumentHandler
{
    struct Weapon
    {
        public string id { get; private set; }
        public int power { get; set; }
        public string name { get; set; }

        public Weapon(string name, int power)
        {
            id = System.Guid.NewGuid().ToString("N");
            this.name = name;
            this.power = power;
        }
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)/resolveDocumentHandler")]
    public static void Run()
    {
        const int MagicPower = 1;
        var weapons = new[]
        {
            new Weapon("Long Bow", 2),
            new Weapon("Short Sword", 3),
            new Weapon("Short Sword", 3 + MagicPower), // We have two weapons that will have different ids, but the same name.
            new Weapon("Long Sword", 4)
        };
        var si = new SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html)("Weapons")
        {
            // Define a handler that returns a searchable string that can search for each document.
            // These words are not indexed, therefore the string is linear and might not scale as expected.
            // IMPORTANT: Unless you want to have case-sensitive search, you should convert the resolved string to lowercase.
            resolveDocumentHandler = (id) => weapons.First(w => w.id == id).name.ToLowerInvariant()
        };

        si.Start();
        foreach (var w in weapons)
        {
            var di = si.AddDocument(w.id);
            si.AddWord("weapon", 0, di);
        }
        si.Finish(() =>
        {
            OnIndexReady(si, weapons);
            // Dispose the SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) when you are done with it.
            si.Dispose();
        });
    }

    private static void OnIndexReady(SearchIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.html) si, Weapon[] weapons)
    {
        var results = si.Search("weapon sword").ToArray();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(results.Length == 3, "No weapon were found");
        foreach (var result in results)
        {
            var w = weapons.First(w => w.id == result.id);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Found [{result.index}] {result.id}/{w.name} ({w.power})");
        }
    }
}

```

* * *
