* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.html

# SearchExpression
class in UnityEditor.Search
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
### Description
Search expressions allow you to add to the search query language to express complex queries that cross-reference multiple providers, for example, to search for all objects in a scene that use a shader that doesn’t compile.  
  
Search expressions can be chained together to transform or perform set manipulations on Search Items.  
  
The manual contains example on [How to use Search Expression](https://docs.unity3d.com/Documentation/Manual/search-expressions.html) .
These examples show how SearchExpression are used in an evaluator:
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

public class SearchExpressionEvaluator_Example
{
    [SearchExpressionEvaluator(SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html) | SearchExpressionType.Variadic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Variadic.html))]
    [SearchExpressionEvaluatorSignatureOverload(SearchExpressionType.Number[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Number.html), SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html) | SearchExpressionType.Variadic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Variadic.html))]
    [Description("Extract and returns the X first results for each expression.")]
    public static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> TakeXFirst(SearchExpressionContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) c)
    {
        var argIndex = 0;
        var takeNumber = 1;
        if (c.args[0].types.HasFlag(SearchExpressionType.Number[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Number.html)))
        {
            ++argIndex;
            takeNumber = Math.Max((int)(c.args[0].GetNumberValue(takeNumber)), 0);
        }

        for ( ; argIndex < c.args.Length; ++argIndex)
        {
            var iterable = c.args[argIndex].Execute(c);
            var taken = 0;
            foreach (var item in iterable)
            {
                if (item == null)
                    yield return null;
                else
                {
                    yield return item;
                    ++taken;
                    if (taken == takeNumber)
                    {
                        c.Break();
                        break;
                    }
                }
            }
        }
    }


    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ExpressionEvaluator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.html)/Take First")]
    static void TestTakeFirst()
    {
        var ctx = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("takexfirst{[1,2,3,4], [34, 45, 66], t:script}");
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(ctx);
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ExpressionEvaluator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.html)/Take 2 First")]
    static void TestTake2First()
    {
        var ctx = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("takexfirst{2, [1,2,3,4], [34, 45, 66], t:script}");
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(ctx);
    }

    [Description("Returns ids of current selection")]
    [SearchExpressionEvaluator(SearchExpressionEvaluationHints.ThreadNotSupported[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluationHints.ThreadNotSupported.html))]
    public static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> SelectionIds(SearchExpressionContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) c)
    {
        var instanceIds = UnityEditor.Selection.instanceIDs;
        foreach (var id in instanceIds)
        {
            yield return SearchExpression.CreateItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.CreateItem.html)(id, c.ResolveAlias("selected id"));
        }
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ExpressionEvaluator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.html)/Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) ids")]
    static void SelectionIds()
    {
        var ctx = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("selectionids{}");
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(ctx);
    }

    [Description("Returns asset paths corresponding to a list of instance ids")]
    [SearchExpressionEvaluator("IdsToPaths", SearchExpressionEvaluationHints.ThreadNotSupported[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionEvaluationHints.ThreadNotSupported.html), SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html))]
    public static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> IdsToPath(SearchExpressionContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) c)
    {
        foreach (var idItem in c.args[0].Execute(c))
        {
            if (SearchExpression.TryConvertToDouble[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.TryConvertToDouble.html)(idItem, out var idNum))
            {
                var id = (int)idNum;
                var path = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(id);
                if (!string.IsNullOrEmpty(path))
                {
                    yield return SearchExpression.CreateItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.CreateItem.html)(path, c.ResolveAlias("asset path"));
                }
            }
        }
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ExpressionEvaluator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.html)/Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) ids to Paths")]
    static void IdsToPaths()
    {
        var ctx = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("IdsToPaths{selectionids{}}");
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(ctx);
    }

    [Description("Convert arguments to a string allowing you to format the result.")]
    [SearchExpressionEvaluator(SearchExpressionType.Selector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Selector.html) | SearchExpressionType.Text[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Text.html), SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html) | SearchExpressionType.Literal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Literal.html) | SearchExpressionType.Variadic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Variadic.html))]
    [SearchExpressionEvaluatorSignatureOverload(SearchExpressionType.Iterable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Iterable.html) | SearchExpressionType.Literal[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Literal.html) | SearchExpressionType.Variadic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionType.Variadic.html))]
    public static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> FormatItems(SearchExpressionContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpressionContext.html) c)
    {
        var skipCount = 0;
        if (SearchExpression.GetFormatString[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.GetFormatString.html)(c.args[0], out var formatStr))
            skipCount++;
        var items = c.args.Skip(skipCount).SelectMany(e => e.Execute(c));
        var dataSet = SearchExpression.ProcessValues[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.ProcessValues.html)(items, null, item => SearchExpression.FormatItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.FormatItem.html)(c.search, item, formatStr));
        return dataSet;
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ExpressionEvaluator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ExpressionEvaluator.html)/Get Script Paths")]
    static void GetScriptPaths()
    {
        var ctx = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("formatitems{t:script search}");
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(ctx);
    }
}

```

### Properties
Property | Description  
---|---  
[alias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression-alias.html) | Alias name of an expression. This is useful to assign a more readable results to methematic expression (lile Count).  
[innerText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression-innerText.html) | This is the inner text of the expression. This means the text without any special delimiters. Ex: the expression [1, 2, 3] which is a set expression would have an innerText of 1,2,3.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression-name.html) | The name of the evaluator function or hte outer text. This is mostly a debuggin field.  
[outerText](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression-outerText.html) | This is the outer text of the expression. This means the full text with any special delimiters. Ex: the expression [1, 2, 3] which is a set expression would have an outerText of [1,2,3].  
[parameters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression-parameters.html) | The parameter list of the expression. Note that each parameter is an expression in itself.  
[types](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression-types.html) | Aggrregate types of the expression. This is mostly used to validate parameters of an expression.  
### Public Methods
Method | Description  
---|---  
[Execute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.Execute.html) | Execute a SearchEXpression givent a certain SearchContext Depending on flags the expression might be valuated in a worker thread (by default) or in the main thread. It returns a an enumerable list of SearchItem.  
[GetBooleanValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.GetBooleanValue.html) | Try to parse the innerText and convert it to a boolean value.  
[GetNumberValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.GetNumberValue.html) | Try to parse the innerText and convert it to a double value.  
[IsKeyword](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.IsKeyword.html) | Check if the innerText of an expression is a builtin SearchExpressionKeyword.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.ToString.html) | Convert an expression to a string representation.  
### Static Methods
Method | Description  
---|---  
[Check](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.Check.html) | Execute a SearchExpression and checks if the internal value of the first yielded SearchItem is truish. Not 0, not null, not "" and not false.  
[CreateId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.CreateId.html) | Generate a unique id. This is useful when creating new SearchItem.  
[CreateItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.CreateItem.html) | Create a new SearchItem from a value with an optional label.  
[FormatItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.FormatItem.html) | Take a format string and replace all selectors in it with the selected values obtained from a SearchItem.  
[GetFormatString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.GetFormatString.html) | Extract a format string from a given expression. This function should be used to extract a format string from an input parameter of a SearchExpression. For example: the evaluator print{"this is it: @label"} takes a format string as its first parameter.  
[IsTrue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.IsTrue.html) | Check if the internal value of a SearchItem is truish. It means the value is not 0, not null, not "" and not false.  
[ProcessValues](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.ProcessValues.html) | Take a group of SearchItems and apply a processHandler transformer function to the item in order to sets its internal value or an outputValueField. Note that these items are processed in the main thread thus allowing you to resolve any kind of selectors.  
[TryConvertToDouble](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchExpression.TryConvertToDouble.html) | Resolve a selector on an item and try to convert the selected value to a double.  
* * *
