// meta.js

// Define your meta title and description here
const metaTitle = "Mission Blue Zone, Neral – Premium Villa Plots with Long-Term ROI";
const metaDescription = "Own 1550 sq. ft. plots in India’s 1st Blue Zone township - Mission Blue Zone by House Of Abhinandan Lodha. Just 2 hrs from Mumbai - Book Now!";


// Function to set meta tags
function setMetaTags() {
    document.title = metaTitle;

    // Set meta description
    let metaDescriptionTag = document.querySelector('meta[name="description"]');
    if (metaDescriptionTag) {
        metaDescriptionTag.setAttribute("content", metaDescription);
    } else {
        metaDescriptionTag = document.createElement('meta');
        metaDescriptionTag.setAttribute("name", "description");
        metaDescriptionTag.setAttribute("content", metaDescription);
        document.head.appendChild(metaDescriptionTag);
    }
}

// Call the function to set meta tags
setMetaTags();