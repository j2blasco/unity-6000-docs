* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html

# SearchContext
class in UnityEditor.Search
Leave feedback
  

Implements interfaces:[ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html)
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
The search context includes all the data necessary to perform a query. It allows the full customization of how a query may be performed.
### Properties
Property | Description  
---|---  
[empty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-empty.html) | Indicates of the search query is empty. This exclude the search filter id. In example if the search text is h: , then this property will still return true.  
[filterId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-filterId.html) | Explicit filter ID. Usually it is the first search token like h:, p: to do an explicit search for a given search provider. Can be null.  
[options](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-options.html) | Search context options.  
[progressId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-progressId.html) | Progress handle to display the progress bar for the search currently in progress.  
[providers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-providers.html) | Which search providers are active for this particular context.  
[searchInProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-searchInProgress.html) | Indicates if an asynchronous search is currently in progress for this context.  
[searchPhrase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-searchPhrase.html) | Returns a phrase that contains only words separated by spaces.  
[searchQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-searchQuery.html) | Processed search query (no filterId, no textFilters).  
[searchQueryOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-searchQueryOffset.html) | Character offset of the processed search query in the raw search text.  
[searchText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-searchText.html) | Raw search text (what is in the Search text box).  
[searchView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-searchView.html) | The search view presenting the search results.  
[searchWords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-searchWords.html) | Search query tokenized by words. All text filters are discarded and all words are in lowercase.  
[selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-selection.html) | Returns the search result selection if any.  
[textFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-textFilters.html) | All tokens containing a colon (':').  
[wantsMore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-wantsMore.html) | Indicates if the search should return all the results instead of only the most relevant.  
### Constructors
Constructor | Description  
---|---  
[SearchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-ctor.html) | Creates a new search context.  
### Public Methods
Method | Description  
---|---  
[AddSearchQueryError](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.AddSearchQueryError.html) | Adds a new query error on this context.  
[AddSearchQueryErrors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.AddSearchQueryErrors.html) | Adds new query errors on this context.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.Dispose.html) | Dispose of the Search Context.  
[IsEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.IsEnabled.html) | Checks if a search provider is available to process a query.  
[SetFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.SetFilter.html) | Enables or disables a single search provider. A disabled search provider won't be asked to provide items to resolve the query.  
### Events
Event | Description  
---|---  
[asyncItemReceived](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-asyncItemReceived.html) | This event is used to receive any asynchronous search result.  
[sessionEnded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-sessionEnded.html) | Invoked when a Search has ended.  
[sessionStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext-sessionStarted.html) | Invoked when a Search is started.  
* * *
