import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";


function Carousel() {
  return (
    <div className="carousel-container my-4">
      <div id="carouselExample" className="carousel slide" data-bs-ride="carousel">
        <div className="carousel-inner rounded-4 shadow-lg">
          {[{
            src: "https://d12d6l12s3d372.cloudfront.net/Virat_Anushka_Myntra_b245b14c74.jpg"          ,
            title: "Shop the Celebrity Style",
            description: "Exclusive fashion inspired by your favorites"
          }, {
            src: "https://i.ytimg.com/vi/v7MGljboQsM/maxresdefault.jpg",
            title: "Top Deals of the Season",
            description: "Get up to 70% off on popular brands"
          }, {
            src: "https://i.ytimg.com/vi/t9g6mu6m1i4/maxresdefault.jpg",
            title: "New Arrivals",
            description: "Be the first to grab the latest trends"
          }].map((item, index) => (
            <div key={index} className={`carousel-item ${index === 0 ? 'active' : ''}`}>
              <img src={item.src} className="d-block w-100 carousel-image" alt={item.title} />
              <div className="carousel-caption custom-caption">
                <h2 className="animated-title">{item.title}</h2>
                <p>{item.description}</p>
              </div>
              <div className="image-overlay"></div>
            </div>
          ))}
        </div>
        <button className="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
          <span className="carousel-control-prev-icon" aria-hidden="true" />
        </button>
        <button className="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
          <span className="carousel-control-next-icon" aria-hidden="true" />
        </button>
      </div>
    </div>
  );
}
export default Carousel;