$(document).ready(function(){
   $(window).bind('scroll', loadOnScroll);
});

// Scroll globals
var pageNum = 1; // The latest page loaded
var tmp = 2;
var hasNextPage = true; // Indicates whether to expect another page after this one
// loadOnScroll handler
var loadOnScroll = function() {
   // If the current scroll position is past out cutoff point...
    if ($(window).scrollTop() > $(document).height() - ($(window).height()*2)) {
        // temporarily unhook the scroll event watcher so we don't call a bunch of times in a row
        $(window).unbind("scroll", loadOnScroll);
        // execute the load function below that will visit the JSON feed and stuff data into the HTML
        loadItems();
    }
};

var loadItems = function() {
    // If the next page doesn't exist, just quit now
    if (hasNextPage === false) {
        return false
    }
    // Update the page number
    pageNum = pageNum + 1;
    mjeseci =["siječnja", "veljače", "ožujka", "travnja", "svibnja", "lipnja", "srpnja", "kolovoza", "rujna", "listopada", "studenog", "prosinca"];
    // Configure the url we're about to hit
    $.ajax({
        url: '',
        data: {page_number: pageNum},
        dataType: 'json',
        success: function(data) {
            // Update global next page variable
            hasNextPage = true;//.hasNext;
            // Loop through all items
            $(".klasa" +pageNum ).after(function(n){
                tmp = pageNum+1
                date = data[n].date.split("-")
                return "<div class='post-preview klasa" + tmp +"'> <a href='objave/" + data[n].id +"'><h2 class='post-title'>" + data[n].title +"</h2><h3 class='post-subtitle'>"data[n].subtitle"</h3></a><p class='post-meta'>Published " + parseInt(date[2], 10) + ". " + mjeseci[date[1]-1] + " " + date[0] + "." + "</p></div>"
            });
        },
        error: function(data) {
            // When I get a 400 back, fail safely
            hasNextPage = false
        },
        complete: function(data, textStatus){
            // Turn the scroll monitor back on
            $(window).bind('scroll', loadOnScroll);

        }
    });
};

console.log('aaa');
