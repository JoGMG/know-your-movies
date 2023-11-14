$(document).ready(() => {
// Home page

    // Implement actions when search-by-button is clicked
    $('.search-by-button').on('click keydown', (event) => {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
            event.preventDefault();
            $('.search-by-dropdown').toggleClass('active');
            $('.search-by-dropdown .separator, .search-by-dropdown input[type="radio"], .search-by-dropdown label').toggleClass('active');
            $('.search-by-button img').toggleClass('rotate');
            $('.search-by-button').toggleClass('radius');
            $('.search-by-overlay').toggleClass('active');
        }
    });
    // Hides .search-by-dropdown when clicked outside its container
    $(document).click((event) => {
        // Check if the clicked element is not inside .search-by-container
        if (!$(event.target).closest('.search-by-container').length) {
            // Hide .search-by-overlay and .search-by-dropdown
            $('.search-by-overlay').removeClass('active');
            $('.search-by-dropdown').removeClass('active');
            $('.search-by-dropdown .separator, .search-by-dropdown input[type="radio"], .search-by-dropdown label').removeClass('active');
            $('.search-by-button img').removeClass('rotate');
            $('.search-by-button').removeClass('radius');
        }
    });

    // Implement actions for checked .search-by-dropdown radio option
    $('input[name="search-by-dropdown-option"]').change(function () {
        if ($(this).is(':checked')) {
            const text = $('.search-by-button-text').text();
            if (!$('.search-by-button-text').html().includes('&nbsp;+1&nbsp;')) {
                $('.search-by-button-text').html(text + '&nbsp;+1&nbsp;');
            }
            $('.search-by-dropdown').addClass('toggle');
        }
    });

    // Changes .search-input background-color on interaction
    $('.search-input').on('focus', () => {
        $('.search-input').addClass('input-color');
    });
    $('.search-input').on('blur', () => {
        $('.search-input').removeClass('input-color');
    });

    // Logo links to homepage when clicked
    $('.logo').on('click keydown', (event) => {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
            event.preventDefault();
            window.location.href = "home_page.html"
        }
    });

    // Retrieves movie details based on search-input value
    $('.search-button, .search-icon').on('click keydown', (event) => {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
            event.preventDefault();
            const keyword = $('.search-input').val();

            // Sets search input to url search query
            const url = new URL("searchresults_page.html", window.location.href);
            url.searchParams.set("search", keyword);
            window.location.href = url.toString();

            if ($('#movie-name').is(':checked')) {
                url.searchParams.set("by", "moviename");
            } else if ($('#cast-name').is(':checked')) {
                url.searchParams.set("by", "castname");
            } else {
                url.searchParams.set("by", "default");
            }
          
            window.location.href = url.toString();
        }
    });

    // Trigger click event on .search-button when in .search-input and enter key is pressed.
    $('.search-input').keypress(function(event) {
        if (event.which === 13) {
            event.preventDefault();
            $('.search-button, .search-icon').click();
        }
    });

// Header search

    // Implement actions when .chevron-button is clicked
    $('.chevron-button').on('click keydown', (event) => {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
            event.preventDefault();
            $('.chevron-button-dropdown').toggleClass('active');
            $('.chevron-button-dropdown .separator, .chevron-button-dropdown input[type="radio"], .chevron-button-dropdown label').toggleClass('active');
            $('.chevron-button img').toggleClass('rotate');
            $('.chevron-button').toggleClass('radius');
            $('.chevron-button-overlay').toggleClass('active');
        }
    });
    // Hides .chevron-button-dropdown when clicked outside its container
    $(document).click((event) => {
        // Check if the clicked element is not inside .chevron-button-container
        if (!$(event.target).closest('.chevron-button-container').length && !$(event.target).closest('.saviour').length) {
            // Hide .chevron-button-overlay and .chevron-button-dropdown
            $('.chevron-button-dropdown').removeClass('active');
            $('.chevron-button-dropdown .separator, .chevron-button-dropdown input[type="radio"], .chevron-button-dropdown label').removeClass('active');
            $('.chevron-button img').removeClass('rotate');
            $('.chevron-button').removeClass('radius');
            $('.chevron-button-overlay').removeClass('active');
        }
    });

    // Changes .search-input-header background-color on interaction
    $('.search-input-header').on('focus', () => {
        $('.search-input-header').addClass('input-color');
    });
    $('.search-input-header').on('blur', () => {
        $('.search-input-header').removeClass('input-color');
    });

    // Check if the current page is "searchresults_page.html"
    if (window.location.pathname.includes("searchresults_page.html")) {

        // Implements actions when interacting with header search
        $('.search-button-header').on('click keydown', (event) => {
            if (event.type === 'click' || event.which === 13 || event.which === 32) {
                event.preventDefault();
                const keyword = $('.search-input-header').val();
    
                // Sets search input to url search query
                const url = new URL("searchresults_page.html", window.location.href);
                url.searchParams.set("search", keyword);

                if ($('#movie-name').is(':checked')) {
                    url.searchParams.set("by", "moviename");
                } else if ($('#cast-name').is(':checked')) {
                    url.searchParams.set("by", "castname");
                } else {
                    url.searchParams.set("by", "default");
                }

                window.location.href = url.toString();
            }
        });

        // Trigger click event on .search-button-header when in .search-input-header and enter key is pressed.
        $('.search-input-header').keypress(function(event) {
            if (event.which === 13) {
                event.preventDefault();
                $('.search-button-header').click();
            }
        });

        // Gets query values
        const urlParams = new URLSearchParams(window.location.search);
        const searchQueryFromURL = urlParams.get('search');
        const byQueryFromURL = urlParams.get('by');

        const searchQuery = searchQueryFromURL;
        if (searchQuery !== null) {
            const headTitleContent = $('title').text();
            $('title').text(`${searchQuery} - ` + headTitleContent + ' Search')

            const searchContainerH1content = $('.searchpage-container h1').text();
            $('.searchpage-container h1').text(searchContainerH1content + `\'${searchQuery}\'`)
        }

        const searchQ = searchQuery.replace(/\s/g, "%20");

        const options = {
            method: 'GET',
            headers: {
            accept: 'application/json',
            Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNTk1NjU1YzhjZmUwYjE4ZmI5Mjg1NDQ4ZTQxMzEyMCIsInN1YiI6IjY1NDdhMzBiMWFjMjkyN2IyZWJjNzJhYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Qm264_ce3ItIPKGeZfL9trSiLiBz05e3wVoUfUxkeJY'
            }
        };

        if (byQueryFromURL === 'moviename' | byQueryFromURL === 'default') {
            // Gets movies based on search query by movie-name
            fetch(`https://api.themoviedb.org/3/search/movie?query=${searchQ}&include_adult=false&language=en-US`, options)
                .then(response => response.json())
                .then(response => {
                    response.results.forEach((data) => {
                        base_url = "https://image.tmdb.org/t/p/w500";
                        const poster = base_url + data.poster_path;
                        const title = data.title;
                        const date = data.release_date;
                        const id = data.id;

                        const newdate = date.split('-')[0];

                        const movieContainer = $('.movie-container');
                        const movieItem = $('<div>').addClass('movie').attr({"tabindex": "0", "data-id": `${id}`});

                        const moviePoster = $('<div>').addClass('movie-poster').html(`<img src="${poster}" alt="${title} poster" onerror="this.src='../dynamic/images/poster-placeholder.png'; this.removeAttribute('alt');"></img>`);
                        const movieTitle = $('<div>').addClass('movie-title').attr({"title": `${title}`}).text(`${title}`);
                        const movieDate = $('<div>').addClass('movie-date').text(`${newdate || '-'}`);

                        movieItem.append(moviePoster).append(movieTitle).append(movieDate);
                        movieContainer.append(movieItem);
                    });
                });
        } else if (byQueryFromURL === 'castname') {
            // Gets movies based on search query by cast-name
            fetch(`https://api.themoviedb.org/3/search/person?query=${searchQ}&include_adult=false&language=en-US`, options)
                .then(response => response.json())
                .then(response => {
                    response.results.forEach((data) => {
                        if (data.known_for_department === 'Acting') {
                            data.known_for.forEach((innerData) => {
                                if (innerData.title !== undefined) {
                                    base_url = "https://image.tmdb.org/t/p/w500";
                                    const poster = base_url + innerData.poster_path;
                                    const title = innerData.title;
                                    const date = innerData.release_date;
                                    const id = innerData.id;
    
                                    const newdate = date.split('-')[0];
    
                                    const movieContainer = $('.movie-container');
                                    const movieItem = $('<div>').addClass('movie').attr({"tabindex": "0", "data-id": `${id}`});
    
                                    const moviePoster = $('<div>').addClass('movie-poster').html(`<img src="${poster}" alt="${title} poster" onerror="this.src='../dynamic/images/poster-placeholder.png'; this.removeAttribute('alt');"></img>`);
                                    const movieTitle = $('<div>').addClass('movie-title').attr({"title": `${title}`}).text(`${title}`);
                                    const movieDate = $('<div>').addClass('movie-date').text(`${newdate || '-'}`);
    
                                    movieItem.append(moviePoster).append(movieTitle).append(movieDate);
                                    movieContainer.append(movieItem);
                                }
                            });
                        }
                    });
                });
        }
    }


// Movies page

    // Click event handler for .movie elements
    $(document).on('click', '.movie', function (event) {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
            // Get the data-id attribute and title value of the clicked .movie element
            const dataId = $(this).attr('data-id');
            const movieT = $(this).find('.movie-title').text();

            // Construct the URL for the new local HTML page using the title and dataId
            const url = `movie_page.html?${movieT}&id=${dataId}`;

            // Redirect to the new page
            window.location.href = url;
        }
    });

    // Check if the current page is "movie_page.html"
    if (window.location.pathname.includes("movie_page.html")) {

        $('.search-button-header').on('click keydown', (event) => {
            if (event.type === 'click' || event.which === 13 || event.which === 32) {
                event.preventDefault();
                const keyword = $('.search-input-header').val();
    
                // Sets search input to url search query
                const url = new URL("searchresults_page.html", window.location.href);
                url.searchParams.set("search", keyword);

                if ($('#movie-name').is(':checked')) {
                    url.searchParams.set("by", "moviename");
                } else if ($('#cast-name').is(':checked')) {
                    url.searchParams.set("by", "castname");
                } else {
                    url.searchParams.set("by", "default");
                }

                window.location.href = url.toString();
            }
        });

        // Trigger click event on .search-button-header when in .search-input-header and enter key is pressed.
        $('.search-input-header').keypress(function(event) {
            if (event.which === 13) {
                event.preventDefault();
                $('.search-button-header').click();
            }
        });

        // # Get search query values.
        const urlParams = new URLSearchParams(window.location.search);
        const IdQuery = urlParams.get('id');

        const options = {
            method: 'GET',
            headers: {
            accept: 'application/json',
            Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNTk1NjU1YzhjZmUwYjE4ZmI5Mjg1NDQ4ZTQxMzEyMCIsInN1YiI6IjY1NDdhMzBiMWFjMjkyN2IyZWJjNzJhYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Qm264_ce3ItIPKGeZfL9trSiLiBz05e3wVoUfUxkeJY'
            }
        };

        // Gets movie details based on movie id
        fetch(`https://api.themoviedb.org/3/movie/${IdQuery}?language=en-US`, options)
            .then(response => response.json())
            .then(response => {
                base_url = "https://image.tmdb.org/t/p/w500";
                const poster = base_url + response.poster_path;
                const title = response.title;
                const date = response.release_date;
                const genre = response.genres;
                const summary = response.overview;

                const newdate = date.split('-')[0];

                const titleContent = $('title').text();
                $('title').text(`${title} - ` + titleContent);

                $('.poster-moviepage').html(`<img src="${poster}" alt="${title} poster" onerror="this.src='../dynamic/images/poster-placeholder.jpg'; this.removeAttribute('alt');"></img>`);
                $('.title-moviepage').html(`<h1>${title}</h1>`);
                $('.date-moviepage').text(newdate);
                $('.genre-moviepage').text(`${genre[0].name}, ${genre[1].name}`);
                $('.summary-moviepage').html(`Summary<p>${summary}</p>`);
            });

        // Gets movies cast details based on movie id
        fetch(`https://api.themoviedb.org/3/movie/${IdQuery}/credits?language=en-US`, options)
            .then(response => response.json())
            .then(response => {
                response.cast.forEach((data) => {
                    if (data.known_for_department === 'Acting') {
                        base_url = "https://image.tmdb.org/t/p/w500";
                        const profile = base_url + data.profile_path;
                        const name = data.name;
                        const character = data.character;
    
                        const cast = $('<div>').addClass('cast');
    
                        const castHeadShot = $('<div>').addClass('cast-headshot').html(`<img src="${profile}" alt="${name} headshot" onerror="this.src='../dynamic/images/headshot-placeholder.png'; this.removeAttribute('alt');">`)
                        const castName = $('<div>').addClass('cast-name').attr({"title": `${name} as ${character}`}).html(`${name}<p><span>as </span>${character}</p>`)
    
                        const allCast = cast.append(castHeadShot).append(castName)
                        $('.cast-container').append(allCast)
                    }
                });

            });

        // Gets movies reviews based on movie id
        fetch(`https://api.themoviedb.org/3/movie/${IdQuery}/reviews?language=en-US`, options)
            .then(response => response.json())
            .then(response => {
                response.results.forEach((data) => {
                    const author = data.author;
                    const text = data.content;
                    const date = data.created_at;

                    const newdate = new Date(date)
                    const newdate_ = newdate.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' });

                    const reviewContainerHeader = $('<div>').addClass('review-container-header');

                    const reviewUserName = $('<div>').addClass('review-username').text(author);
                    const reviewDate = $('<div>').addClass('review-date').text(newdate_);

                    const reviewTextContainer = $('<div>').addClass('review-text-container');
                    const fullReviewText = $('<pre>').addClass('review-text').attr({"tabindex": "0"}).text(text);
                    const shortenedReviewContainer = $('<pre>').addClass('review-text-shortened-container').attr({"tabindex": "0"});

                    let shortenedText
                    if (text.length > 200) {
                        shortenedText = text.slice(0, 200);
                    } else {
                        shortenedText = text
                    }

                    const shortenedReviewText = $('<span>').addClass('review-text-shortened').text(shortenedText);
                    const moreIcon = $('<a>').addClass('more-icon').attr({"role": "button", "tabindex": "0"}).text('...More');

                    reviewContainerHeader.append(reviewUserName).append(reviewDate);
                    $('.review-quote-container').before(reviewContainerHeader);

                    if (shortenedText.length < 200) {
                        shortenedReviewContainer.append(shortenedReviewText)
                    } else {
                        shortenedReviewContainer.append(shortenedReviewText).append(moreIcon);
                    }

                    reviewTextContainer.append(fullReviewText).append(shortenedReviewContainer);

                    $('.right-quote-icon').before(reviewTextContainer);
                });

            });

        // Implement actions when .leave-a-review-button is clicked
        $(document).on('click keydown', '.leave-a-review-button', (event) => {
            if (event.type === 'click' || event.which === 13 || event.which === 32) {
                event.preventDefault();
                $('.review-container').hide();
                $('.leave-a-review-container').show();
            }
        });

        // Implement actions when #close-icon is clicked
        $(document).on('click keydown', '#close-icon',(event) => {
            if (event.type === 'click' || event.which === 13 || event.which === 32) {
                event.preventDefault();
                $('.leave-a-review-container').hide();
                $('.review-container').show();
            }
        });

        // Implements a toggle feature
        let isExpanded = false;

        $(document).on('click keydown', '.review-text-shortened-container, .review-text', (event) => {
            if (event.type === 'click' || event.which === 13 || event.which === 32) {
                event.preventDefault();
                const textReview = $(event.target).closest('.review-text-container').find('.review-text');
                const shortenedTextReviewContainer = $(event.target).closest('.review-text-container').find('.review-text-shortened-container');

                if (textReview.text().length > 200 ) {
                    if (isExpanded) {
                        textReview.hide();
                        shortenedTextReviewContainer.show();
                        isExpanded = false
                    } else {
                        shortenedTextReviewContainer.hide();
                        textReview.show();
                        isExpanded = true;
                    }
                } else {
                    textReview.hide();
                    shortenedTextReviewContainer.show();
                    isExpanded = false;
                }
            }
        });

        // Implements an automatic .review-text-container slide
        let textIndex = 0;

        $('.saviour').on('click', (event) => {
            const reviewTextContainer = $(event.target).closest('.review-container').find('.review-text-container');
            const reviewContainerHeader = $(event.target).closest('.review-container').find('.review-container-header')

            reviewTextContainer.hide().removeClass('active');
            reviewContainerHeader.hide().removeClass('active');

            textIndex++;
            if (textIndex > reviewTextContainer.length) {
                textIndex = 1;
            }
            reviewTextContainer.eq(textIndex - 1).show().addClass('active');
            reviewContainerHeader.eq(textIndex - 1).show().addClass('active');
        });

        let intervalId;

        function startInterval() {
            intervalId = setInterval(function() {
                $('.saviour').trigger('click');
            }, 5000);
        }

        startInterval();

        // Stop the interval function when hovering over .review-container
        $('.review-container').mouseenter(function() {
            clearInterval(intervalId);
        });

        // Continue the interval function when not hovering over .review-container
        $('.review-container').mouseleave(function() {
            startInterval();
        });

        // Implements a manual .review-text-container slide
        function manualSlide(n) {
            const reviewTextContainer = $(event.target).closest('.review-container').find('.review-text-container');
            const reviewContainerHeader = $(event.target).closest('.review-container').find('.review-container-header')

            reviewTextContainer.hide().removeClass('active');
            reviewContainerHeader.hide().removeClass('active');

            if (n > reviewTextContainer.length) {
                n = 1;
            }
            if (n < 1) {
                n = reviewTextContainer.length;
            }

            reviewTextContainer.eq(n - 1).show().addClass('active');
            reviewContainerHeader.eq(n - 1).show().addClass('active');
        }

        // Implements next/previous controls for manualSlide
        function changeSlide(n) {
            textIndex = n;  // Upadates manualSlide (from autoSlide)
            manualSlide(n)
        }

        $(document).on('click keydown', '.prev', (event) => {
            if (event.type === 'click' || event.which === 13 || event.which === 32) {
                event.preventDefault();
                changeSlide(textIndex - 1)
            }
        });

        $(document).on('click keydown', '.next', (event) => {
            if (event.type === 'click' || event.which === 13 || event.which === 32) {
                event.preventDefault();
                changeSlide(textIndex + 1)
            }
        });
    }
});
