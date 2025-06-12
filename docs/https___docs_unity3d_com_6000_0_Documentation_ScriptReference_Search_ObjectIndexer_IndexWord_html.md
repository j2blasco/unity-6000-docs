* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.IndexWord.html

#  [ObjectIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html).IndexWord
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
## Declaration
public void IndexWord(int documentIndex, ref string word, bool exact, int scoreModifier); 
### Parameters
Parameter | Description  
---|---  
documentIndex | Document where the indexed word was found.  
word | Word to add to the index.  
exact | If true, we will also store an exact match entry for this word.  
scoreModifier | Modified to apply to the base match score for a specific word.  
### Description
Adds a new word coming from a specific document to the index. The word will be added with multiple variations allowing partial search.
The following example indexes a word that can be used to search indexed prefabs with `myawesomeword`, `myawe`, etc.
```
[CustomObjectIndexer(typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)))]
static void IndexGameObject(CustomObjectIndexerTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) target, ObjectIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) indexer)
{
    var go = target.target as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
    if (go == null)
        return;

    indexer.AddWord("myawesomeword", 0, target.documentIndex);
}

```

* * *
## Declaration
public void IndexWord(int documentIndex, ref string word, int maxVariations, bool exact, int scoreModifier); 
### Parameters
Parameter | Description  
---|---  
documentIndex | Document where the indexed word was found.  
word | Word to add to the index.  
maxVariations |  **Maximum number of variations to compute. Cannot be higher than the length of the word.**  
exact | If true, the indexer will also store an exact match entry for this word.  
scoreModifier | Modified to apply to the base match score for a specific word.  
### Description
The word will be added with a maximum of variation. This can be used to save some space for very large words.
* * *
