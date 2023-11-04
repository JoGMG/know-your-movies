# Know Your Movies - Movie Cast Discovery

## Introduction

Welcome to "Know Your Movies," a project aimed at helping users discover movie casts with a simple click. Whether you're a movie enthusiast, student, content creator, or casting director, our platform provides a quick way to view the cast of a movie. No more struggling to remember actors' names – we've got you covered!

## Team Members and Roles

- **UX Designer**: Frank Kaziputa
- **Front-End Developer**: David Oluwatosin Dorcas
- **Back-End Developer**: Joshua Attah

## Technologies Used

- **Libraries**: jQuery (JavaScript library)
- **Languages**: Python, MySQL, HTML, CSS, JS
- **Framework**: Flask
- **Books**: Python for Dummies, Automate Everything with Python
- **Resources**: Man Pages

## Alternatives

- **Django instead of Flask**: While Flask is minimalistic, Django offers more built-in features.
- **MongoDB instead of MySQL**: MongoDB is a NoSQL database, while MySQL uses structured data.

## Problem Statement

### What We Intend to Solve

We want to help users find out the cast of movies they've watched with ease. "Know Your Movies" provides a one-click solution to discover movie casts.

### What We Don't Intend to Solve

We do not aim to be a movie streaming platform or provide movie downloads.

## Users

Our platform is designed for:

- Movie Enthusiasts
- Students
- Content Creators
- Casting Directors
- And many others.

## Risks

### Technical Risks

- **Data Accuracy**: Inaccurate data may misinform users.
  - *Preventive Measures*: Use multiple data sources and encourage user feedback for data validation.

- **Scalability**: As data increases, the server and database must scale accordingly.
  - *Preventive Measures*: Implement load balancing to handle server performance.

### Non-Technical Risks

- **Negative User Reviews**: Negative experiences can lead to poor reviews.
  - *Preventive Measures*: Ensure data accuracy and address user complaints promptly.

- **User Experience**: Lack of language support can frustrate users.
  - *Preventive Measure*: Implement language translation features.

## Infrastructure

### Branching and Merging Process

We follow the GitHub Flow, a lightweight, branch-based workflow for efficient collaboration and code deployment. The key steps include:

1. Create a Branch
2. Add Commits
3. Pull Request (PR)
4. Review and Discussion
5. Merge
6. Delete Branch

This workflow ensures collaboration, code quality, and correctness.

### Deployment Strategy

We implement Continuous Deployment (CD) where code changes are automatically deployed to production after passing automated tests.

### Data Population Strategy

Data is sourced from various places, including API integration, the site's database, and user-generated data through reviews.

### Testing Tool

We employ Unit Testing to ensure individual software components perform as intended.

## Existing Solutions

We are similar to existing movie-related websites like IMDb, The Movie Database, Rotten Tomatoes, and Metacritic in that we provide cast information and encourage user reviews. However, our focus on movie casts simplifies the user experience by providing precise information without unnecessary complexity.

## License

public

---
