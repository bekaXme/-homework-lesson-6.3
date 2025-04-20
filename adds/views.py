from django.http import HttpResponse

def show(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Centered Navbar Example</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
    <nav class='navbar navbar-expand-lg navbar-light bg-light'>
      <div class='container'>
        <div class='collapse navbar-collapse justify-content-center' id='navbarSupportedContent'>
          <ul class='navbar-nav mb-2 mb-lg-0'>
            <li class='nav-item'>
              <a class='nav-link active' href='/first/'>1 - page</a>
            </li>
            <li class='nav-item'>
              <a class='nav-link active' href='/second/'>2 - page</a>
            </li>
            <li class='nav-item'>
              <a class='nav-link active' href='/third/'>3 - page</a>
            </li>
            <li class='nav-item'>
              <a class='nav-link active' href='/fourth/'>4 - page</a>
            </li>
            <li class='nav-item'>
              <a class='nav-link active' href='/fifth/'>5 - page</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    </body>
    </html>
    """)


def first(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>1 - Page</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <nav class='navbar navbar-expand-lg navbar-light bg-light'>
            <div class='container'>
                <div class='collapse navbar-collapse justify-content-center' id='navbarSupportedContent'>
                    <ul class='navbar-nav mb-2 mb-lg-0'>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/first'>1 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/second/'>2 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/third/'>3 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fourth/'>4 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fifth/'>5 - page</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <h1>Welcome to Page 1</h1>
            <p>This is the first page of the website. Here you can put any content you'd like — such as information about your website, a welcome message, or a description of services.</p>

            <div class="card mt-4">
              <div class="card-body">
                <h5 class="card-title">About Us</h5>
                <p class="card-text">We are a team dedicated to providing top-quality service and information. Our mission is to build beautiful, responsive web applications using Django and Bootstrap.</p>
              </div>
            </div>
        </div>
    </body>
    </html>
    """)
    
    
def second(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>2 - Page</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <nav class='navbar navbar-expand-lg navbar-light bg-light'>
            <div class='container'>
                <div class='collapse navbar-collapse justify-content-center' id='navbarSupportedContent'>
                    <ul class='navbar-nav mb-2 mb-lg-0'>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/first/'>1 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/second/'>2 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/third/'>3 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fourth/'>4 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fifth/'>5 - page</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <h1>Welcome to Page 2</h1>
            <p>This is the second page of the website. Here you can showcase your services, updates, or team information.</p>

            <div class="card mt-4">
              <div class="card-body">
                <h5 class="card-title">Our Services</h5>
                <p class="card-text">We offer web development, mobile app development, and UI/UX design services using modern frameworks and best practices. Our focus is on delivering quality and user-friendly solutions.</p>
              </div>
            </div>
        </div>
    </body>
    </html>
    """)
    
def third(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>3 - Page</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <style>
            .fun-card {
                transition: transform 0.3s ease;
            }
            .fun-card:hover {
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <nav class='navbar navbar-expand-lg navbar-light bg-light'>
            <div class='container'>
                <div class='collapse navbar-collapse justify-content-center' id='navbarSupportedContent'>
                    <ul class='navbar-nav mb-2 mb-lg-0'>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/first/'>1 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/second/'>2 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/third/'>3 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fourth/'>4 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fifth/'>5 - page</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <h1 class="text-center mb-4">🎉 Fun Facts About Technology 🎉</h1>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card fun-card shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">💡 Did You Know?</h5>
                            <p class="card-text">The first computer virus was created in 1986 and was called “Brain.” It was made by two brothers in Pakistan.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card fun-card shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">🌐 Internet Speed</h5>
                            <p class="card-text">The fastest internet speed ever recorded is 319 Terabits per second — that’s enough to download Netflix's entire library in seconds!</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card fun-card shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">📱 Smartphone Power</h5>
                            <p class="card-text">Modern smartphones are more powerful than the computers used during the Apollo 11 moon landing in 1969.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)

def fourth(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>4 - Page</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <nav class='navbar navbar-expand-lg navbar-light bg-light'>
            <div class='container'>
                <div class='collapse navbar-collapse justify-content-center' id='navbarSupportedContent'>
                    <ul class='navbar-nav mb-2 mb-lg-0'>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/first/'>1 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/second/'>2 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/third/'>3 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fourth/'>4 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fifth/'>5 - page</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <h2 class="text-center">📞 Contact Us</h2>
            <p class="text-center text-muted">Have questions or suggestions? Drop us a message!</p>

            <form class="mt-4 col-md-8 offset-md-2">
                <div class="mb-3">
                    <label for="name" class="form-label">Your Name</label>
                    <input type="text" class="form-control" id="name" placeholder="John Doe">
                </div>
                <div class="mb-3">
                    <label for="email" class="form-label">Your Email</label>
                    <input type="email" class="form-control" id="email" placeholder="example@email.com">
                </div>
                <div class="mb-3">
                    <label for="message" class="form-label">Your Message</label>
                    <textarea class="form-control" id="message" rows="4" placeholder="Type your message here..."></textarea>
                </div>
                <button type="submit" class="btn btn-primary w-100">Send Message</button>
            </form>

            <div class="text-center mt-5">
                <p>📧 Email: contact@yourwebsite.com</p>
                <p>📍 Address: 123 Web Street, Code City, Devland</p>
                <p>⏰ Open: Mon - Fri (9 AM - 6 PM)</p>
            </div>
        </div>
    </body>
    </html>
    """)

def fifth(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>5 - Page</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
        <nav class='navbar navbar-expand-lg navbar-light bg-light'>
            <div class='container'>
                <div class='collapse navbar-collapse justify-content-center' id='navbarSupportedContent'>
                    <ul class='navbar-nav mb-2 mb-lg-0'>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/first/'>1 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/second/'>2 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/third/'>3 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fourth/'>4 - page</a>
                        </li>
                        <li class='nav-item'>
                            <a class='nav-link active' href='/fifth/'>5 - page</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <div class="container mt-5">
            <h2 class="text-center mb-4">🌟 Photo Gallery</h2>
            <div class="row row-cols-1 row-cols-md-3 g-4">

                <div class="col">
                    <div class="card">
                        <img src="https://picsum.photos/300/200?random=1" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">City Lights</h5>
                            <p class="card-text">Experience the beauty of the night city view captured in vibrant colors.</p>
                        </div>
                    </div>
                </div>

                <div class="col">
                    <div class="card">
                        <img src="https://picsum.photos/300/200?random=2" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Nature Escape</h5>
                            <p class="card-text">Breathe in the freshness of untouched nature and peaceful forests.</p>
                        </div>
                    </div>
                </div>

                <div class="col">
                    <div class="card">
                        <img src="https://picsum.photos/300/200?random=3" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Ocean Breeze</h5>
                            <p class="card-text">Feel the calm of ocean waves crashing gently on the golden shore.</p>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </body>
    </html>
    """)

