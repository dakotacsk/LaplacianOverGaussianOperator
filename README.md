# QEA2_LaplacianOverGaussianOperator

This repository contains the `QEA2_LaplacianOverGaussianOperator` package, which provides tools for edge detection in images using the Laplacian of Gaussian (LoG) method. It's designed for educational purposes to demonstrate the principles of image processing in the context of QEA.

## Installation

You can install the `QEA2_LaplacianOverGaussianOperator` directly from this GitHub repository using `pip`. Ensure you have `pip` and `Git` installed on your system before proceeding.

To install the package, run the following command:

```
pip install git+https://github.com/dcoder0111/LaplacianOverGaussianOperator.git#egg=LaplacianOverGaussianOperator
```

## Usage

Example usage is shown in example_usage.py. More documentation about the mathematical reasoning behind the code and these filters are provided in the [TeachingMaterials](TeachingMaterial) folder.

## Examples

An example image `spherical_cow.jpeg` is included in the `img/` directory to help you get started with the package. You can use this image to test the functionality of the edge detection algorithm.

Here are some things you can generate with this library:
Original Image:
![An unmodified image Olin College's Miller Academic Center](https://github.com/dcoder0111/QEA2_LaplacianOverGaussianOperator/blob/main/img/examples/Olin.jpeg?raw=true)

Sobel and Laplacian Applied to Image:
![An image of Olin College's Miller Academic Center with LoG applied](https://github.com/dcoder0111/QEA2_LaplacianOverGaussianOperator/blob/main/img/examples/Olin_Derivatives.png?raw=true)

LoG Applied with Different Sigma Values:
![An image of Olin College's Miller Academic Center with LoG applied](https://github.com/dcoder0111/QEA2_LaplacianOverGaussianOperator/blob/main/img/examples/Olin_LoG.png?raw=true)


## Repo Structure

```
QEA2_LaplacianOverGaussianOperator /
│
├── edge_detection/
│   └── __init__.py
│
├── img/
│   └── spherical_cow.jpeg # used in example_usuage.py
│
├── example_usage.py
│
└── setup.py
```

## Contributing

Contributions to the `QEA2_LaplacianOverGaussianOperator` package are welcome! If you'd like to contribute, please fork the repository and use a new branch for your contributions. Pull requests are warmly welcomed.

## License

This project is licensed under the MIT License - see the `LICENSE` file in the repository for details.

## Acknowledgments

- This package was developed as part of the Quantitative Engineering and Analysis (QEA) course.
- Special thanks to all contributors and users of this package.
