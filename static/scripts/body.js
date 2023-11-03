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
    $('input[name="search-by-dropdown-option"]').change(() => {
        if ($(this).is(':checked')) {
            const text = $('.search-by-button').text();
            if (!$('.search-by-button').html().includes('&nbsp;+1')) {
                $('.search-by-button-text').html(text + '&nbsp;+1');
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
        if (!$(event.target).closest('.chevron-button-container').length) {
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


// Movies page

    // Implement actions when .leave-a-review-button is clicked
    $('.leave-a-review-button').on('click keydown', (event) => {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
          event.preventDefault();
          $('.review-container').hide();
          $('.leave-a-review-container').show();
        }
    });

    // Implement actions when #close-icon is clicked
    $('#close-icon').on('click keydown', (event) => {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
          event.preventDefault();
          $('.leave-a-review-container').hide();
          $('.review-container').show();
        }
    });

    // Review texts
    const reviews = [
        {
            userName: "James Lough",
            date: "23 February, 2023",
            text: "The Dark Knight is Christopher Nolan's magnum opus and a gripping, unforgettable thrill ride from start to finish.\n\nThe acting performances in this film are truly as great as they come. Heath Ledgers infamous take on the Joker is undoubtedly one of the most captivating, disturbing, and iconic villain performances in film history. All of the other main players in the film (especially Batman, Harvey Dent, and Commissioner Gordon) are also acted remarkably well, due in part to the immense strength of the film's cast.\n\nThe action and stunt-work in this film are utterly spectacular. Few other films have ever managed to keep me on the edge of my seat this much during chases, and fight scenes. There are a number of reasons for this. Christopher Nolan clearly put a lot of work into the stunts in this film and it shows. Every jaw dropping explosion, or nail biting vehicle chase feels as if it is really happening and that you are experiencing it in real time with the characters. The music is undoubtedly some of the best I have ever heard in a film. The all time great film composer Hans Zimmer once again proves to be a master of his craft here, delivering a thoroughly blood pumping and epic musical score that enhances the action ten fold.\n\nThe storytelling is some of the best in the history of comic book filmmaking. It is dark, unforgettable, and exceptionally intricate. The film tackles very mature themes that are far beyond most comic book movies, such as the contrast between order and chaos, as well as whether superheroes are truly heroes or simply vigilantes. The characters are also ALL masterfully well written. Many of the characters, such as Harvey Dent, Commissioner Gordon, and Batman, embark on some of the greatest and most thought provoking character arcs I have ever seen. The richly detailed world building surrounding Gotham city also helps to make the film feel remarkably immersive (especially for a superhero movie).\n\nOverall the Dark Knight is without a doubt one of the greatest films of the last century and an essential film experience, even for those who are not fans of the superhero genre. It is legendary for a reason"
        },
        {
            userName: "AJ Taylor",
            date: "17 July, 2023",
            text: "I can't believe that today marks the 15-year anniversary of the release of Christopher Nolan's game-changing comic book movie \"The Dark Knight,\" and watching it again for the umpteenth time this morning it really is a groundbreaking achievement from both a genre standpoint but also a technical aspect. This film has a grand scale visual style to it that most comic book/superhero films fail to capture due to the excessive use of CGI and VFX, whereas here Nolan and his crew told a grounded story that somehow has a larger than life feel to it without the use of digital effects and it's an epic on the scale of a David Lean film while being ten toes to the ground in the vein of Michael Mann's \"Heat.\"\n\nStarting off where the previous film \"Batman Begins\" ended, we are introduced to the iconic nemesis to the Dark Knight in Joker who is a true agent of chaos and looks to prove that anyone who deems themselves to be a moral and ethical person is one bad day away from being an anarchist and he looks to prove that by wreaking havoc throughout Gotham, and this film gave us one of the all-time performances from the late great Heath Ledger as the Clown Prince of Crime. I could rave about his performance alone in this post, but simply put it's an actor showcasing the depths of his talents and being someone you can't take your eyes off whenever he's on screen and being the only posthumous Oscar win for an actor in film history as he left behind a legacy role that will never be outdone, but I feel as if Christian Bale as Batman and especially Aaron Eckhart as Harvey Dent get overlooked due to the greatness of Ledger's Joker as they are truly amazing here with Bruce's arc seeing him encounter a foe that is much more than he ever bargained for and recognizing that he has limits while Dent's arc sees him go from Gotham's white knight to a monster named Two-Face in a tragic downfall like never before. The recasting of Maggie Gyllenhaal as Rachel Dawes is one I've always championed and she proves to be better than Katie Holmes in the role while Gary Oldman as Commissioner Gordon gets an even bigger role here.\n\nHans Zimmer's music in this film has become synonymous with the character as the score feels triumphant yet cynical, while Wally Pfister's cinematography gives this the crime noir look needed to tell this dark story but this is not the flawless film that I thought it was during its release as there are a lot of plot holes and conveniences that force the audience to just take a leap and go with it. The Joker being able to rig bombs in a hospital unrecognized and even getting into the hospital unidentified has never made any sense for this to be a grounded story, and how Batman failed to know the dirty cops on the force when he's the World's Greatest Detective has baffled me for quite a while and in addition the fight choreography mixed with the choppy editing make for these lifeless combat scenes that don't highlight the martial arts and fight specialist that Batman is as well as that terrible voice used by Bale. Negatives aside, this is still a film that is important to both cinema and the superhero genre as a whole."
        },
        {
            userName: "Pat Cahill",
            date: "3 October, 2022",
            text: "Why it rocks:\n\nIt's often considered the greatest comic-book movie of all time.\n\nOne of the most successful attempts to make a superhero movie appear realistic.\n\nThe Major Highlight: Heath Ledger's portrayal of the Joker is arguably the best and greatest incarnation of the Joker character to date. Ledger made an outstanding job portraying the Joker as insane and unpredictable yet utterly terrifying and menacing through his impeccable method acting skills. All of the scenes featuring him (Like the monologues about his scars or when he talks to Harvey Dent at the hospital) are extremely tense and keep you at the edge of your seat, not to mention that nearly all of his dialogue is memorable and quotable. He got a very deserved Oscar for the role, becoming the first comic-book movie actor to do so.Great scenery.\n\nGreat editing.\n\nAwesome dialogue.\n\nAmazing cinematography.\n\nExcellent fight scenes.\n\nThe film's dark and gritty tone was done right.\n\nFantastic direction from Christopher Nolan; this has become his most iconic movie.\n\nMemorable and now iconic scenes, some of them include: The opening bank robbery, the Joker's pencil trick, the truck chase, Batman interrogating the Joker, the hospital explosion, etc.\n\nIt updates the batsuit to closer resemble the logo symbol and the batarang itself. They even explain this in the film by having Bruce ask Lucius for a more flexible suit.\n\nRachel's death was an unexpected moment that majorly affects Batman for the rest of the trilogy.\n\nAll of the action sequences are very exciting and fun to watch.\n\nExcellent score composed by Hans Zimmer and James Newton Howard.\n\nThe acting is great all around; and while Ledger is the one who stands out the most, the truth is that everyone in this movie is absolutely fantastic. From Christian Bale, Gary Oldman, Aaron Eckhart, Michael Caine and Maggie Gyllenhaal.\n\nTwo-Face is also a great and intimidating villain that is driven by revenge instead of his split-personality disorder getting worst after his face is burned.\n\nMemorable qoutes."
        }
    ];

    // Creates .review-text-container along with its elements
    reviews.forEach(review => {
        const userName = review.userName;
        const date = review.date;
        const reviewText = review.text;

        const reviewContainerHeader = $('<div>').addClass('review-container-header');

        const reviewUserName = $('<div>').addClass('review-username').text(userName);
        const reviewDate = $('<div>').addClass('review-date').text(date);

        const reviewTextContainer = $('<div>').addClass('review-text-container');
        const fullReviewText = $('<pre>').addClass('review-text').attr({"tabindex": "0"}).text(reviewText);
        const shortenedReviewContainer = $('<pre>').addClass('review-text-shortened-container').attr({"tabindex": "0"});

        const shortenedText = reviewText.slice(0, 200);
        const shortenedReviewText = $('<span>').addClass('review-text-shortened').text(shortenedText);
        const moreIcon = $('<a>').addClass('more-icon').attr({"role": "button", "tabindex": "0"}).text('...More');

        reviewContainerHeader.append(reviewUserName).append(reviewDate);
        $('.review-quote-container').before(reviewContainerHeader);

        shortenedReviewContainer.append(shortenedReviewText).append(moreIcon);
        reviewTextContainer.append(fullReviewText).append(shortenedReviewContainer);

        $('.right-quote-icon').before(reviewTextContainer);
    });

    // Implements a toggle feature
    let isExpanded = false;
    const textReview = $('.review-text');
    const shortenedTextReviewContainer = $('.review-text-shortened-container');

    $('.review-text-shortened-container, .review-text').on('click keydown', (event) => {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
            event.preventDefault();
            if (isExpanded) {
                textReview.hide();
                shortenedTextReviewContainer.show();
                isExpanded = false
            } else {
                shortenedTextReviewContainer.hide();
                textReview.show();
                isExpanded = true;
            }
        }
    });

    // Implements an automatic .review-text-container slide
    const reviewTextContainer = $('.review-text-container');
    const reviewContainerHeader = $('.review-container-header')
    let textIndex = 0;
    let slideTimeout;

    function autoSlide() {
        reviewTextContainer.hide();
        reviewTextContainer.removeClass('active');
        
        reviewContainerHeader.hide();
        reviewContainerHeader.removeClass('active');

        textIndex++;
        if (textIndex > reviewTextContainer.length) {
            textIndex = 1;
        }
        reviewTextContainer.eq(textIndex - 1).show();
        reviewTextContainer.eq(textIndex - 1).addClass('active');

        reviewContainerHeader.eq(textIndex - 1).show();
        reviewContainerHeader.eq(textIndex - 1).addClass('active');

        slideTimeout = setTimeout(autoSlide, 5000);
    }

    // Implements a manual .review-text-container slide
    function manualSlide(n) {
        reviewTextContainer.hide();
        reviewTextContainer.removeClass('active');

        reviewContainerHeader.hide();
        reviewContainerHeader.removeClass('active');

        if (n > reviewTextContainer.length) {
            n = 1;
        }
        if (n < 1) {
            n = reviewTextContainer.length;
        }
        reviewTextContainer.eq(n - 1).show();
        reviewTextContainer.eq(textIndex - 1).addClass('active');

        reviewContainerHeader.eq(textIndex - 1).show();
        reviewContainerHeader.eq(textIndex - 1).addClass('active');
    }

    // Implements next/previous controls for manualSlide
    function changeSlide(n) {
        textIndex = n;  // Upadates manualSlide (from autoSlide)
        manualSlide(n)
    }

    $('.prev').on('click keydown', (event) => {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
            event.preventDefault();
            changeSlide(textIndex - 1)
        }
    });

    $('.next').on('click keydown', (event) => {
        if (event.type === 'click' || event.which === 13 || event.which === 32) {
            event.preventDefault();
            changeSlide(textIndex + 1)
        }
    });

    // Pause/resume slide on .review-container hover
    $('.review-container').hover(
        function() {
            clearTimeout(slideTimeout); // Pause sliding
        },
        function() {
            autoSlide(); // Resume sliding
        }
    );

    autoSlide();
});
