import numpy as np
import matplotlib.pyplot as plt

x = [78, 113, 36, 88, 105, 26, 31, 118, 100, 76, 36, 72, 94, 38, 38, 110, 222, 112, 97, 252, 114, 73, 89, 73, 45, 93, 64, 122, 19, 53, 193, 101, 242, 131, 306, 232, 42, 68, 60, 50, 119, 45, 103, 20, 155, 117, 310, 93, 32, 22, 55, 108, 121, 279, 61, 66, 75, 20, 69, 215, 160, 80, 39, 235, 194, 89, 19, 86, 195, 98, 34, 91, 133, 54, 77, 43, 137, 41, 111, 87, 70, 95, 578, 144, 177, 105, 164, 257, 69, 26, 149, 42, 148, 103, 65, 128, 77, 46, 108, 42, 189, 111, 55, 48, 338, 21, 44, 62, 49, 132, 54, 65, 42, 80, 59, 59, 82, 183, 67, 231, 105, 79, 263, 49, 79, 36, 100, 57, 101, 94, 27, 50, 39, 23, 140, 87, 82, 54, 71, 164, 32, 96, 72, 165, 72, 47, 127, 107, 282, 122, 130, 223, 181, 64, 53, 50, 88, 69, 120, 141, 117, 51, 189, 120, 32, 74, 158, 179, 82, 120, 36, 210, 379, 78, 123, 65, 86, 141, 74, 115, 144, 137, 114, 179, 57, 86, 45, 63, 47, 38, 100, 76, 146, 33, 373, 81, 200, 154, 129, 152, 104, 32, 88, 247, 56, 170, 150, 122, 41, 415, 35, 76, 59, 126, 53, 153, 211, 360, 110, 175, 33, 136, 145, 157, 52, 62, 232, 123, 62, 14, 68, 76, 150, 112, 45, 32, 34, 49, 62, 155, 33, 325, 67, 85, 39, 105, 173, 74, 127, 29, 43, 30, 65, 141, 42, 78, 87, 152, 98, 238, 45, 21, 105, 62, 106, 44, 68, 228, 20, 67, 59, 114, 64, 107, 110, 108, 80, 134, 147, 165, 22, 53, 70, 130, 17, 93, 71, 165, 80, 81, 136, 61, 189, 56, 63, 92, 49, 56, 123, 155, 357, 36, 76, 38, 76, 122, 167, 104, 82, 43, 100, 92, 45, 138, 148, 156, 175, 109, 31, 110, 57, 30, 48, 43, 71, 107, 61, 53, 52, 257, 188, 26, 18, 92, 74, 207, 64, 32, 62, 103, 43, 83, 154, 99, 34, 17, 42, 114, 56, 66, 46, 64, 108, 65, 149, 40, 56, 52, 79, 165, 57, 176, 130, 65, 45, 72, 99, 32, 49, 62, 133, 40, 149, 69, 59, 80, 74, 104, 97, 51, 72, 23, 35, 154, 229, 128, 69, 141, 49, 29, 141, 61, 245, 125, 35, 109, 63, 80, 72, 110, 375, 40, 104, 229, 94, 235, 223, 50, 229, 29, 58, 84, 67, 86, 187, 80, 23, 60, 124, 138, 105, 41, 48, 64, 34, 173, 66, 52, 108, 80, 28, 168, 146, 206, 295, 38, 83, 214, 39, 35, 112, 188, 42, 350, 135, 179, 117, 31, 40, 41, 23, 206, 119, 109, 41, 221, 100, 42, 62, 122, 19, 118, 37, 27, 21, 67, 102, 50, 142, 58, 44, 88, 114, 22, 140, 43, 106, 112, 124, 116, 72, 49, 106, 38, 54, 53, 67, 21, 50, 81, 35, 33, 46, 49, 78, 74, 53, 42, 24, 80, 91, 190, 64, 54, 170, 31, 42, 61, 23, 160, 86, 99, 88, 85, 108, 105, 203, 73, 38, 303, 93, 341, 81, 146, 48, 67, 83, 40, 369, 41, 246, 32, 93, 62, 44, 88, 138, 38, 81, 59, 190, 120, 74, 53, 44, 197, 373, 124, 65, 30, 56, 232, 88, 33, 125, 67, 108, 53, 81, 119, 36, 36, 52, 163, 55, 35, 27, 141, 139, 31, 182, 101, 21, 84, 187, 219, 59, 238, 212, 70, 59, 144, 131, 29, 57, 162, 339, 113, 66, 335, 283, 341, 100, 31, 63, 81, 46, 39, 123, 79, 18, 180, 131, 90, 49, 112, 193, 73, 159, 108, 199, 219, 67, 214, 72, 84, 28, 55, 37, 109, 465, 48, 97, 112, 147, 23, 39, 114, 17, 62, 62, 53, 123, 59, 198, 42, 117, 38, 33, 167, 121, 148, 79, 239, 61, 74, 103, 27, 359, 68, 56, 35, 94, 103, 157, 128, 86, 29, 84, 78, 112, 100, 194, 149, 60, 125, 135, 83, 162, 122, 87, 73, 166, 61, 18, 93, 23, 38, 185, 60, 276, 176, 111, 47, 229, 79, 84, 87, 143, 90, 200, 166, 37, 147, 116, 59, 456, 23, 72, 71, 39, 137, 184, 36, 19, 38, 74, 164, 176, 53, 152, 217, 47, 38, 239, 54, 29, 173, 198, 137, 102, 71, 89, 236, 213, 62, 120, 48, 112, 63, 78, 46, 275, 80, 91, 59, 98, 49, 121, 124, 348, 25, 35, 87, 105, 64, 448, 30, 62, 38, 86, 98, 51, 20, 61, 31, 39, 42, 433, 146, 49, 126, 113, 102, 58, 48, 94, 103, 60, 122, 88, 189, 45, 108, 87, 80, 151, 81, 116, 86, 95, 38, 123, 117, 42, 58, 383, 81, 81, 30, 216, 285, 163, 139, 55, 66, 196, 176, 131, 114, 47, 127, 24, 175, 169, 78, 53, 73, 82, 127, 86, 30, 36, 257, 124, 72, 89, 81, 107, 34, 291, 24, 65, 256, 37, 101, 73, 165, 25, 141, 43, 116, 265, 38, 33, 36, 72, 37, 74, 72, 67, 163, 86, 267, 29, 69, 97, 128, 37, 74, 197, 69, 69, 287, 64, 113, 117, 58, 35, 63, 60, 184, 129, 128, 57, 116, 74, 84, 111, 44, 391, 167, 120, 79, 63, 56, 326, 25, 139, 100, 117, 187, 138, 226, 28, 60, 123, 35, 80, 114, 159, 107, 215, 94, 128, 249, 47, 43, 79, 43, 47, 164, 169, 171, 53, 131, 177, 56, 174, 55, 57, 108, 77, 38, 83, 39, 90, 90, 66, 76, 78, 38, 54, 31, 233, 26, 139, 39, 39, 64, 25, 34, 69, 242, 145, 124, 28, 33, 110, 61, 52, 46, 157, 40, 53, 32, 225, 159, 76, 64, 127, 200, 169, 220, 80, 71, 32, 170, 49, 20, 51, 65, 152, 42, 144, 42, 40, 53, 48, 193, 51, 110, 82, 33, 123, 51, 69, 100, 68, 56, 372, 131, 30, 50, 63, 46, 111, 82, 45, 158, 104, 102, 108, 111, 175, 52, 87, 38, 38, 122, 304, 73, 34, 78, 92, 125, 103, 250, 148, 161, 87, 136, 50, 100, 68, 255, 297, 183, 141, 70, 46, 105, 35, 38, 47, 294, 99, 93, 77, 51, 137, 164, 108, 51, 89, 98, 158, 123, 93, 95, 227, 57, 116, 56, 56, 26, 61, 76, 100, 106, 204, 191, 59, 33, 197, 98, 157, 102, 46, 46, 168, 174, 33, 56, 93, 175, 61, 67, 315, 177, 41, 50, 100, 142, 84, 44, 39, 56, 100, 53, 56, 182, 93, 62, 31, 20, 156, 44, 68, 40, 263, 42, 97, 69, 56, 45, 107, 98, 244, 48, 31, 93, 204, 95, 203, 33, 164, 62, 171, 32, 47, 67, 49, 229, 177, 92, 21, 42, 22, 136, 144, 174, 278, 26, 56, 90, 135, 137, 384, 93, 62, 137, 67, 115, 360, 94, 66, 77, 95, 128, 154, 61, 161, 79, 43, 158, 139, 31, 152, 60, 58, 50, 107, 72, 131, 156, 240, 166, 63, 26, 42, 85, 226, 47, 117, 149, 106, 25, 97, 31, 36, 74, 60, 54, 75, 40, 89, 113, 138, 153, 45, 177, 124, 122, 118, 54, 174, 74, 121, 42, 100, 112, 102, 33, 120, 67, 14, 34, 71, 53, 149, 54, 63, 231, 152, 109, 118, 327, 70, 59, 355, 336, 186, 102, 224, 89, 84, 80, 66, 142, 19, 242, 155, 88, 58, 44, 148, 101, 120, 28, 36, 26, 85, 48, 195, 234, 42, 185, 322, 95, 169, 111, 67, 313, 76, 77, 66, 43, 84, 42, 62, 25, 45, 152, 144, 65, 78, 179, 106, 65, 95, 230, 59, 180, 43, 49, 46, 52, 77, 264, 87, 55, 86, 104, 133, 64, 91, 47, 222, 121, 53, 107, 147, 44, 225, 134, 123, 45, 120, 10, 44, 54, 90, 348, 45, 52, 67, 88, 477, 144, 106, 141, 28, 26, 58, 133, 110, 80, 94, 364, 145, 61, 122, 278, 110, 48, 100, 71, 67, 75, 121, 52, 94, 209, 91, 42, 87, 95, 107, 241, 112, 55, 20, 47, 78, 248, 24, 77, 280, 43, 36, 82, 33, 102, 61, 38, 201, 113, 69, 42, 25, 114, 106, 255, 90, 184, 218, 48, 201, 52, 42, 104, 83, 214, 117, 80, 151, 276, 26, 158, 281, 71, 142, 48, 340, 35, 40, 32, 30, 332, 86, 63, 31, 43, 39, 111, 98, 45, 71, 72, 88, 41, 215, 116, 118, 86, 241, 70, 119, 146, 93, 75, 33, 35, 261, 71, 87, 89, 52, 64, 113, 108, 201, 43, 38, 180, 158, 56, 70, 221, 81, 182, 85, 104, 232, 149, 122, 171, 39, 177, 73, 175, 54, 260, 134, 49, 37, 108, 58, 44, 205, 77, 59, 163, 35, 222, 56, 48, 215, 99, 143, 58, 92, 164, 61, 39, 113, 131, 24, 30, 82, 292, 217, 55, 136, 90, 33, 191, 73, 63, 380, 176, 52, 127, 133, 426, 58, 49, 29, 81, 123, 41, 150, 244, 128, 448, 95, 29, 51, 201, 111, 27, 104, 78, 81, 80, 231, 45, 173, 246, 70, 52, 83, 55, 60, 34, 367, 27, 160, 52, 199, 160, 65, 128, 68, 199, 107, 56, 104, 65, 43, 109, 61, 147, 46, 259, 65, 88, 106, 55, 43, 30, 155, 113, 61, 98, 178, 98, 148, 27, 184, 73, 26, 73, 132, 53, 65, 73, 37, 71, 32, 23, 234, 286, 39, 72, 184, 175, 115, 32, 113, 163, 58, 85, 51, 67, 40, 60, 173, 148, 37, 251, 183, 18, 96, 178, 68, 149, 307, 54, 28, 31, 185, 417, 70, 68, 145, 63, 216, 36, 87, 80, 201, 37, 150, 54, 27, 217, 154, 134, 136, 132, 61, 78, 53, 66, 58, 176, 35, 276, 93, 194, 33, 191, 252, 472, 95, 88, 18, 77, 25, 28, 102, 27, 45, 133, 83, 64, 68, 22, 81, 61, 79, 205, 226, 56, 71, 75, 89, 208, 47, 90, 27, 154, 234, 119, 88, 96, 38, 78, 57, 118, 136, 143, 66, 26, 374, 109, 54, 50, 55, 75, 54, 53, 85, 96, 46, 67, 57, 142, 67, 30, 44, 54, 117, 75, 119, 105, 141, 158, 62, 183, 295, 99, 159, 53, 117, 137, 102, 97, 127, 266, 19, 66, 229, 40, 98, 165, 41, 46, 180, 38, 72, 79, 156, 82, 215, 151, 95, 50, 64, 90, 56, 98, 314, 27, 38, 96, 144, 189, 207, 111, 48, 53, 80, 21, 29, 226, 77, 71, 118, 75, 143, 134, 240, 116, 46, 112, 67, 94, 47, 22, 51, 93, 63, 106, 152, 36, 115, 54, 92, 138, 36, 29, 79, 76, 178, 44, 62, 133, 173, 39, 169, 203, 49, 103, 47, 60, 94, 197, 71, 87, 53, 75, 49, 126, 173, 168, 36, 206, 140, 188, 108, 93, 43, 58, 55, 51, 96, 36, 67, 228, 223, 109, 37, 102, 219, 258, 38, 57, 116, 37, 81, 160, 126, 86, 140, 72, 83, 118, 47, 83, 38, 76, 47, 147, 118, 90, 39, 74, 53, 255, 80, 221, 49, 111, 41, 50, 49, 271, 91, 60, 50, 64, 71, 61, 92, 76, 169, 76, 81, 36, 54, 44, 78, 74, 49, 34, 425, 116, 38, 35, 46, 162, 21, 57, 24, 54, 27, 72, 64, 60, 58, 69, 343, 230, 43, 231, 49, 275, 46, 123, 102, 16, 79, 56, 77, 131, 132, 119, 93, 191, 99, 46, 151, 33, 198, 65, 36, 170, 301, 67, 75, 61, 86, 250, 31, 251, 48, 42, 125, 123, 81, 74, 141, 113, 126, 141, 129, 83, 99, 71, 29, 148, 142, 116, 254, 44, 86, 126, 95, 48, 40, 83, 126, 130, 77, 117, 24, 65, 77, 114, 64, 70, 82, 260, 36, 33, 43, 84, 37, 135, 25, 380, 131, 50, 337, 40, 83, 231, 76, 62, 55, 72, 148, 40, 99, 137, 63, 198, 187, 62, 53, 111, 32, 111, 160, 52, 246, 81, 27, 177, 21, 83, 244, 159, 145, 197, 77, 44, 144, 185, 108, 244, 45, 52, 299, 90, 176, 75, 175, 128, 63, 192, 36, 81, 80, 180, 40, 93, 27, 52, 26, 137, 42, 93, 54, 197, 67, 78, 74, 83, 34, 30, 32, 65, 66, 89, 231, 41, 165, 184, 97, 101, 107, 216, 168, 37, 83, 108, 32, 97, 48, 154, 81, 118, 30, 78, 262, 152, 45, 372, 138, 57, 33, 53, 89, 75, 75, 36, 114, 57, 62, 25, 191, 69, 49, 67, 59, 97, 72, 39, 96, 23, 60, 73, 129, 134, 118, 26, 236, 78, 133, 263, 233, 36, 28, 47, 77, 41, 460, 69, 115, 151, 119, 114, 36, 61, 56, 112, 71, 166, 124, 94, 110, 186, 28, 15, 44, 27, 285, 81, 133, 93, 72, 171, 64, 58, 72, 373, 32, 31, 38, 78, 155, 179, 80, 147, 48, 36, 104, 248, 114, 49, 66, 52, 49, 106, 41, 46, 83, 174, 266, 86, 82, 140, 71, 179, 81, 70, 74, 124, 67, 32, 176, 70, 148, 100, 97, 71, 139, 98, 243, 108, 54, 27, 83, 78, 60, 84, 43, 38, 114, 61, 63, 77, 33, 380, 35, 100, 118, 60, 77, 293, 161, 76, 90, 196, 95, 99, 34, 95, 216, 52, 56, 65, 21, 14, 56, 210, 180, 127, 66, 38, 84, 67, 214, 52, 59, 99, 77, 42, 84, 103, 128, 198, 148, 77, 62, 112, 178, 11, 72, 139, 74, 34, 81, 74, 83, 39, 83, 91, 32, 86, 71, 35, 308, 166, 189, 57, 338, 324, 77, 166, 24, 38, 33, 123, 42, 34, 94, 63, 110, 54, 50, 68, 36, 94, 280, 65, 52, 121, 165, 102, 51, 99, 97, 61, 124, 67, 18, 167, 39, 128, 65, 43, 116, 325, 98, 82, 183, 191, 274, 69, 102, 136, 41, 101, 92, 18, 31, 31, 33, 59, 27, 70, 175, 118, 169, 128, 177, 61, 72, 77, 49, 188, 111, 34, 131, 73, 292, 123, 66, 132, 39, 156, 119, 62, 147, 102, 118, 198, 92, 137, 352, 212, 180, 36, 65, 139, 40, 114, 295, 58, 100, 129, 157, 145, 30, 88, 136, 64, 208, 442, 62, 276, 185, 69, 217, 73, 61, 200, 23, 59, 44, 135, 44, 40, 164, 130, 51, 118, 109, 71, 67, 98, 81, 190, 28, 46, 25, 88, 105, 163, 174, 75, 47, 62, 47, 112, 129, 66, 39, 90, 56, 87, 59, 171, 118, 28, 142, 58, 18, 105, 91, 126, 167, 64, 65, 72, 189, 50, 221, 123, 97, 327, 107, 59, 147, 61, 32, 107, 166, 89, 62, 34, 203, 101, 165, 108, 137, 96, 21, 99, 74, 61, 63, 269, 53, 62, 66, 59, 97, 97, 75, 50, 98, 70, 95, 137, 95, 169, 43, 331, 25, 48, 59, 38, 52, 44, 57, 71, 148, 49, 70, 53, 66, 98, 55, 63, 292, 114, 54, 46, 89, 183, 79, 166, 55, 92, 179, 152, 89, 26, 31, 65, 80, 25, 101, 24, 138, 29, 117, 35, 42, 153, 82, 85, 58, 147, 32, 171, 223, 64, 218, 119, 97, 44, 56, 150, 80, 175, 158, 59, 230, 59, 77, 166, 44, 67, 39, 56, 136, 56, 112, 159, 124, 135, 92, 86, 63, 79, 399, 139, 255, 106, 100, 254, 172, 153, 48, 34, 59, 63, 306, 166, 262, 22, 202, 77, 111, 62, 375, 22, 82, 66, 56, 57, 75, 77, 109, 20, 88, 51, 60, 91, 191, 83, 29, 105, 270, 106, 96, 109, 65, 71, 147, 106, 157, 252, 93, 68, 64, 59, 54, 81, 81, 49, 111, 271, 115, 91, 97, 222, 54, 102, 33, 53, 135, 55, 311, 82, 76, 71, 77, 58, 168, 93, 84, 79, 99, 78, 362, 18, 135, 73, 106, 58, 109, 79, 78, 42, 83, 220, 64, 54, 49, 35, 82, 60, 162, 78, 85, 155, 127, 275, 107, 129, 115, 108, 66, 86, 87, 61, 61, 72, 187, 229, 83, 57, 41, 38, 97, 38, 92, 29, 43, 55, 104, 81, 29, 49, 75, 131, 44, 51, 148, 107, 182, 26, 95, 123, 113, 120, 65, 53, 85, 68, 51, 41, 33, 64, 152, 45, 68, 81, 77, 62, 122, 61, 68, 30, 237, 75, 97, 84, 55, 123, 88, 109, 104, 29, 61, 98, 41, 369, 44, 47, 46, 26, 33, 78, 28, 143, 112, 164, 71, 44, 37, 106, 66, 63, 34, 143, 146, 88, 266, 53, 132, 432, 74, 42, 74, 53, 58, 123, 120, 104, 144, 56, 38, 57, 139, 102, 52, 28, 129, 47, 45, 189, 126, 46, 146, 41, 280, 77, 107, 52, 113, 39, 30, 125, 125, 61, 238, 130, 111, 59, 131, 45, 52, 44, 76, 65, 126, 227, 228, 28, 178, 68, 50, 113, 96, 70, 125, 85, 111, 97, 124, 192, 37, 301, 179, 38, 26, 46, 59, 56, 104, 198, 34, 91, 90, 36, 66, 84, 40, 105, 154, 117, 97, 288, 109, 52, 137, 138, 64, 37, 66, 76, 123, 162, 50, 93, 311, 42, 121, 172, 191, 51, 125, 207, 71, 60, 59, 84, 44, 67, 184, 24, 94, 102, 56, 290, 67, 44, 40, 42, 31, 106, 326, 91, 94, 94, 71, 52, 112, 144, 118, 77, 101, 86, 237, 68, 165, 52, 134, 90, 52, 89, 86, 65, 61, 101, 296, 77, 65, 153, 65, 45, 63, 94, 83, 362, 66, 317, 233, 36, 86, 18, 110, 250, 174, 88, 192, 74, 124, 65, 258, 115, 175, 52, 85, 51, 153, 78, 41, 42, 76, 109, 37, 65, 31, 65, 359, 72, 74, 70, 81, 42, 272, 45, 32, 65, 58, 35, 47, 79, 55, 72, 42, 110, 138, 109, 97, 43, 280, 77, 281, 48, 72, 476, 266, 53, 94, 99, 58, 130, 47, 58, 98, 115, 39, 233, 70, 88, 122, 78, 148, 32, 41, 209, 51, 98, 54, 149, 17, 100, 83, 124, 202, 65, 277, 89, 113, 35, 79, 21, 42, 212, 50, 48, 57, 146, 130, 82, 87, 161, 82, 116, 48, 70, 52, 46, 52, 201, 78, 80, 82, 116, 200, 56, 79, 82, 85, 46, 144, 19, 119, 85, 50, 49, 96, 220, 78, 106, 32, 91, 100, 101, 32, 43, 185, 41, 63, 84, 153, 53, 79, 85, 46, 99, 48, 211, 214, 62, 37, 167, 62, 73, 108, 24, 254, 21, 214, 75, 54, 77, 113, 148, 82, 110, 230, 111, 89, 58, 103, 96, 26, 81, 83, 56, 243, 135, 117, 21, 120, 156, 73, 121, 48, 68, 25, 80, 98, 105, 37, 453, 124, 167, 143, 121, 51, 44, 82, 98, 428, 63, 90, 84, 129, 49, 114, 84, 29, 295, 52, 114, 66, 62, 42, 53, 216, 104, 43, 57, 91, 41, 257, 95, 33, 95, 231, 47, 230, 60, 69, 49, 33, 17, 260, 94, 62, 159, 49, 34, 52, 175, 74, 139, 389, 94, 79, 125, 188, 60, 181, 79, 34, 108, 95, 20, 110, 78, 106, 80, 65, 82, 74, 374, 34, 45, 63, 96, 333, 129, 50, 194, 118, 79, 204, 90, 16, 136, 34, 169, 174, 42, 69, 123, 54, 55, 51, 34, 90, 78, 208, 295, 103, 42, 31, 79, 132, 79, 70, 45, 279, 34, 211, 75, 81, 41, 34, 68, 147, 108, 97, 57, 109, 87, 106, 41, 161, 151, 32, 71, 163, 57, 51, 41, 38, 44, 49, 35, 49, 256, 269, 64, 56, 34, 213, 70, 203, 253, 34, 128, 95, 174, 32, 192, 48, 141, 248, 196, 44, 87, 80, 42, 70, 61, 217, 257, 108, 122, 102, 72, 59, 58, 34, 57, 194, 41, 28, 56, 66, 17, 283, 256, 201, 122, 118, 43, 57, 95, 78, 96, 230, 49, 127, 172, 154, 99, 43, 167, 354, 76, 53, 154, 91, 45, 102, 86, 67, 134, 89, 154, 235, 102, 214, 45, 262, 71, 147, 100, 105, 191, 190, 101, 52, 51, 75, 260, 78, 88, 40, 48, 60, 383, 93, 42, 39, 170, 83, 129, 23, 45, 67, 70, 171, 258, 173, 99, 55, 51, 82, 294, 27, 54, 67, 294, 205, 242, 93, 60, 27, 70, 35, 50, 93, 80, 67, 126, 161, 58, 70, 214, 27, 182, 171, 17, 32, 187, 42, 115, 103, 54, 143, 155, 91, 159, 63, 37, 173, 73, 49, 165, 162, 111, 232, 91, 89, 179, 91, 78, 119, 75, 234, 124, 216, 46, 76, 66, 106, 144, 94, 130, 29, 46, 287, 212, 33, 71, 38, 108, 24, 157, 139, 274, 94, 286, 55, 82, 36, 374, 57, 125, 48, 45, 94, 115, 272, 32, 69, 37, 66, 64, 303, 35, 129, 87, 51, 243, 74, 35, 67, 82, 160, 58, 102, 124, 105, 44, 99, 368, 147, 236, 63, 37, 236, 104, 166, 72, 249, 76, 256, 161, 64, 53, 79, 18, 74, 143, 34, 110, 72, 51, 108, 175, 245, 122, 118, 95, 183, 195, 50, 24, 99, 85, 21, 47, 106, 348, 185, 63, 17, 85, 61, 132, 34, 171, 124, 104, 155, 167, 102, 420, 78, 270, 39, 98, 289, 159, 65, 43, 35, 40, 308, 75, 220, 54, 141, 54, 102, 59, 47, 91, 278, 39, 159, 181, 222, 43, 36, 100, 68, 37, 51, 32, 138, 132, 27, 78, 118, 113, 40, 36, 106, 68, 66, 88, 119, 161, 249, 43, 40, 166, 23, 43, 128, 64, 113, 144, 65, 121, 98, 46, 42, 78, 79, 67, 93, 204, 153, 262, 44, 113, 67, 40, 50, 350, 54, 76, 74, 53, 77, 187, 250, 60, 96, 62, 40, 38, 133, 112, 143, 53, 47, 45, 172, 327, 53, 81, 82, 54, 56, 169, 56, 375, 81, 29, 51, 115, 213, 82, 78, 269, 48, 48, 92, 219, 63, 411, 209, 60, 36, 122, 192, 51, 51, 118, 93, 67, 135, 23, 32, 342, 59, 60, 279, 123, 137, 44, 68, 101, 41, 46, 99, 60, 94, 41, 36, 67, 216, 84, 115, 89, 159, 45, 94, 180, 111, 52, 45, 64, 214, 154, 53, 103, 198, 86, 221, 98, 112, 70, 79, 30, 85, 76, 111, 22, 55, 49, 43, 75, 64, 55, 28, 57, 89, 185, 88, 103, 28, 86, 100, 90, 330, 33, 305, 60, 101, 31, 91, 148, 31, 42, 52, 45, 45, 39, 277, 77, 96, 35, 50, 184, 419, 126, 97, 49, 75, 94, 69, 220, 32, 219, 114, 48, 22, 101, 37, 62, 112, 63, 127, 265, 134, 97, 18, 115, 21, 40, 160, 168, 76, 81, 264, 103, 202, 138, 80, 130, 35, 27, 98, 221, 71, 62, 158, 73, 102, 31, 158, 26, 110, 76, 31, 66, 173, 92, 27, 75, 106, 142, 57, 133, 95, 80, 148, 68, 45, 26, 49, 65, 188, 50, 54, 66, 91, 105, 56, 81, 161, 53, 87, 45, 204, 71, 66, 45, 177, 165, 329, 53, 130, 57, 58, 145, 58, 76, 84, 42, 30, 125, 158, 53, 32, 244, 27, 87, 70, 177, 55, 123, 84, 67, 57, 173, 45, 110, 78, 139, 58, 129, 45, 210, 191, 161, 93, 94, 67, 24, 77, 41, 165, 158, 93, 65, 82, 73, 91, 73, 341, 167, 75, 129, 322, 165, 110, 70, 20, 174, 106, 28, 30, 96, 150, 91, 57, 232, 85, 226, 84, 26, 58, 26, 45, 26, 77, 124, 127, 60, 122, 29, 64, 21, 99, 86, 247, 33, 30, 167, 191, 49, 157, 137, 98, 74, 207, 257,
     56, 181, 64, 28, 223, 187, 94, 116, 108, 51, 62, 143, 92, 78, 502, 142, 128, 57, 78, 33, 14, 21, 490, 54, 72, 72, 75, 129, 100, 83, 104, 53, 101, 95, 82, 64, 77, 35, 43, 191, 66, 50, 28, 121, 168, 113, 68, 59, 58, 155, 165, 75, 45, 105, 98, 69, 50, 137, 135, 187, 240, 85, 63, 20, 90, 52, 251, 128, 35, 79, 29, 69, 75, 75, 57, 43, 64, 135, 57, 83, 35, 100, 67, 116, 381, 264, 47, 273, 155, 129, 63, 106, 121, 242, 130, 147, 48, 55, 214, 30, 45, 90, 139, 88, 81, 70, 92, 44, 108, 133, 29, 31, 121, 51, 133, 43, 68, 133, 29, 170, 55, 204, 42, 100, 80, 78, 245, 41, 132, 65, 23, 99, 44, 51, 108, 36, 51, 221, 190, 67, 180, 45, 72, 179, 84, 74, 32, 201, 76, 69, 346, 75, 56, 31, 82, 76, 159, 22, 88, 150, 296, 126, 195, 43, 141, 47, 29, 45, 198, 202, 276, 24, 105, 54, 57, 73, 32, 67, 77, 76, 22, 74, 124, 129, 52, 27, 59, 81, 67, 106, 103, 25, 157, 64, 37, 47, 134, 49, 220, 60, 186, 49, 67, 212, 94, 60, 53, 48, 59, 142, 56, 64, 63, 32, 107, 96, 70, 62, 186, 99, 80, 86, 57, 100, 162, 52, 102, 130, 33, 84, 433, 20, 168, 49, 31, 21, 23, 93, 84, 98, 127, 130, 473, 47, 236, 68, 59, 38, 99, 54, 39, 67, 105, 76, 276, 245, 141, 48, 60, 124, 55, 26, 103, 63, 224, 41, 125, 243, 164, 80, 108, 130, 89, 156, 67, 77, 94, 92, 35, 217, 68, 165, 18, 98, 76, 40, 85, 35, 271, 92, 50, 23, 34, 95, 115, 19, 76, 61, 41, 286, 46, 115, 40, 101, 108, 244, 140, 261, 156, 53, 182, 97, 55, 58, 99, 95, 39, 259, 69, 41, 61, 72, 56, 39, 84, 78, 61, 32, 153, 113, 58, 133, 184, 157, 111, 92, 48, 107, 147, 45, 91, 112, 140, 47, 41, 81, 18, 46, 218, 79, 84, 149, 60, 128, 95, 53, 56, 82, 252, 111, 118, 31, 62, 37, 128, 78, 49, 83, 31, 93, 24, 81, 91, 245, 165, 61, 164, 49, 58, 35, 72, 143, 81, 59, 67, 72, 137, 192, 162, 134, 35, 239, 112, 79, 44, 32, 135, 50, 168, 169, 66, 106, 40, 36, 73, 49, 214, 141, 62, 185, 57, 153, 42, 63, 118, 81, 77, 59, 129, 31, 28, 318, 150, 41, 166, 101, 99, 16, 87, 151, 70, 164, 244, 31, 129, 25, 165, 30, 34, 26, 69, 57, 84, 93, 164, 105, 61, 161, 26, 84, 40, 100, 40, 119, 122, 142, 56, 105, 35, 85, 292, 57, 84, 53, 43, 40, 62, 56, 105, 42, 69, 30, 77, 37, 63, 198, 86, 170, 87, 43, 67, 178, 57, 44, 52, 35, 118, 152, 185, 61, 59, 76, 100, 54, 24, 258, 41, 47, 245, 182, 71, 71, 281, 123, 247, 97, 165, 270, 110, 162, 71, 43, 153, 38, 120, 58, 113, 45, 88, 50, 91, 64, 19, 78, 29, 54, 56, 65, 59, 115, 135, 19, 56, 68, 74, 94, 114, 69, 145, 90, 132, 107, 31, 54, 126, 111, 184, 100, 158, 35, 164, 208, 31, 74, 88, 99, 47, 547, 114, 30, 26, 109, 64, 67, 170, 72, 44, 265, 86, 248, 187, 130, 220, 164, 142, 46, 231, 26, 23, 196, 95, 188, 58, 84, 150, 28, 80, 104, 62, 69, 36, 104, 169, 65, 30, 155, 164, 56, 29, 73, 153, 49, 98, 38, 35, 58, 210, 206, 22, 57, 80, 128, 145, 43, 93, 156, 126, 42, 38, 219, 55, 79, 278, 90, 119, 62, 171, 120, 29, 49, 262, 358, 74, 82, 98, 95, 113, 17, 84, 52, 260, 68, 41, 17, 42, 41, 133, 62, 103, 58, 146, 41, 44, 134, 485, 98, 27, 81, 32, 93, 45, 98, 185, 35, 40, 133, 48, 81, 38, 123, 135, 19, 126, 77, 30, 46, 42, 41, 103, 53, 57, 66, 81, 45, 204, 67, 72, 154, 88, 35, 120, 525, 38, 231, 120, 81, 71, 122, 524, 164, 112, 63, 320, 269, 113, 112, 86, 27, 61, 56, 92, 153, 26, 50, 38, 76, 43, 42, 125, 85, 157, 74, 46, 52, 51, 161, 208, 23, 89, 67, 23, 97, 318, 157, 73, 84, 71, 66, 348, 24, 53, 126, 33, 124, 124, 91, 110, 73, 116, 28, 100, 75, 201, 66, 60, 221, 71, 35, 172, 61, 135, 232, 100, 194, 213, 125, 130, 107, 268, 68, 40, 192, 30, 50, 117, 59, 36, 68, 79, 31, 41, 57, 41, 83, 98, 64, 76, 36, 65, 32, 275, 186, 70, 58, 39, 132, 114, 68, 146, 63, 188, 63, 89, 162, 64, 61, 32, 66, 93, 122, 60, 68, 58, 68, 132, 32, 173, 85, 229, 141, 127, 47, 75, 41, 201, 181, 29, 139, 112, 71, 66, 57, 54, 34, 89, 47, 234, 132, 248, 46, 55, 22, 111, 119, 52, 98, 118, 159, 69, 250, 138, 159, 155, 86, 159, 98, 50, 33, 38, 77, 86, 105, 43, 357, 49, 155, 133, 78, 105, 70, 102, 29, 116, 27, 204, 120, 96, 127, 32, 100, 63, 35, 121, 41, 190, 132, 193, 94, 34, 56, 103, 30, 145, 236, 105, 309, 98, 141, 94, 98, 136, 78, 21, 60, 56, 43, 132, 49, 30, 80, 72, 111, 77, 137, 30, 60, 89, 24, 55, 40, 161, 66, 45, 55, 163, 34, 138, 220, 292, 194, 61, 43, 52, 68, 43, 89, 157, 89, 163, 61, 35, 96, 44, 140, 21, 78, 60, 168, 73, 105, 28, 334, 59, 68, 31, 47, 70, 204, 190, 108, 48, 67, 100, 57, 44, 64, 219, 115, 193, 105, 55, 24, 68, 317, 265, 141, 46, 163, 66, 159, 53, 69, 41, 84, 113, 75, 31, 43, 94, 68, 47, 193, 241, 86, 137, 65, 125, 355, 54, 116, 158, 90, 42, 301, 133, 24, 24, 68, 92, 44, 238, 119, 53, 50, 31, 86, 51, 73, 132, 84, 99, 64, 57, 102, 23, 36, 43, 155, 29, 31, 44, 69, 139, 84, 116, 182, 35, 132, 73, 91, 40, 176, 168, 108, 31, 95, 101, 28, 53, 49, 27, 81, 65, 172, 293, 231, 47, 77, 253, 37, 33, 188, 50, 85, 92, 49, 48, 35, 186, 48, 18, 75, 43, 36, 45, 47, 71, 129, 61, 65, 30, 87, 178, 65, 85, 62, 110, 56, 99, 32, 80, 272, 217, 91, 63, 107, 72, 246, 165, 37, 207, 35, 115, 27, 72, 62, 40, 225, 120, 373, 26, 98, 117, 149, 78, 61, 92, 102, 119, 65, 31, 109, 65, 110, 46, 40, 66, 123, 65, 134, 91, 99, 58, 112, 82, 88, 34, 189, 35, 63, 86, 158, 141, 196, 101, 87, 60, 288, 114, 99, 150, 87, 161, 181, 84, 115, 25, 124, 80, 288, 201, 174, 124, 49, 187, 27, 141, 120, 102, 73, 252, 178, 293, 186, 40, 119, 32, 109, 105, 62, 70, 40, 17, 105, 38, 57, 79, 140, 245, 150, 34, 38, 49, 25, 88, 55, 56, 46, 134, 462, 244, 107, 53, 162, 29, 54, 140, 26, 143, 85, 119, 183, 68, 68, 24, 193, 71, 154, 107, 146, 273, 96, 48, 44, 43, 41, 119, 78, 247, 164, 84, 134, 48, 59, 87, 121, 163, 44, 113, 208, 162, 47, 78, 104, 110, 61, 44, 142, 212, 56, 61, 46, 73, 77, 141, 63, 270, 213, 79, 105, 55, 26, 122, 204, 161, 60, 35, 82, 140, 186, 86, 76, 61, 75, 41, 88, 134, 126, 133, 90, 51, 52, 36, 89, 49, 84, 88, 137, 42, 63, 305, 43, 137, 194, 47, 87, 39, 118, 89, 42, 18, 227, 109, 131, 32, 53, 65, 148, 40, 23, 68, 269, 134, 145, 73, 121, 334, 113, 78, 39, 261, 27, 39, 94, 97, 216, 25, 145, 54, 167, 45, 66, 225, 251, 64, 67, 119, 213, 49, 20, 40, 82, 149, 108, 104, 86, 99, 95, 26, 158, 88, 211, 46, 29, 41, 21, 21, 70, 349, 127, 124, 53, 57, 167, 200, 87, 60, 151, 41, 267, 74, 30, 147, 89, 73, 167, 50, 36, 137, 57, 112, 53, 188, 83, 35, 177, 174, 20, 72, 56, 28, 85, 220, 411, 154, 71, 182, 209, 57, 249, 34, 25, 158, 56, 126, 97, 26, 139, 38, 135, 52, 331, 140, 83, 198, 160, 255, 61, 96, 52, 46, 26, 155, 57, 41, 121, 42, 69, 39, 41, 256, 192, 43, 80, 52, 172, 152, 83, 114, 377, 46, 133, 57, 74, 34, 40, 68, 56, 47, 136, 116, 87, 149, 52, 53, 82, 78, 48, 277, 19, 51, 89, 44, 454, 119, 80, 82, 121, 60, 232, 26, 302, 56, 152, 88, 268, 42, 128, 80, 134, 38, 519, 143, 88, 81, 39, 88, 37, 30, 175, 48, 62, 261, 215, 123, 129, 181, 111, 83, 64, 178, 35, 657, 102, 106, 543, 56, 68, 159, 66, 119, 196, 25, 201, 44, 64, 86, 32, 153, 102, 205, 57, 27, 131, 40, 111, 195, 373, 77, 328, 75, 116, 245, 51, 196, 165, 156, 133, 79, 200, 317, 92, 136, 24, 119, 244, 63, 57, 94, 193, 97, 63, 40, 194, 122, 39, 196, 199, 252, 170, 61, 29, 64, 231, 150, 38, 215, 146, 43, 88, 55, 98, 42, 53, 46, 168, 164, 148, 34, 147, 68, 41, 83, 90, 37, 33, 220, 56, 43, 71, 22, 86, 353, 116, 67, 213, 155, 112, 89, 123, 61, 161, 223, 91, 52, 49, 34, 42, 434, 53, 78, 117, 54, 223, 217, 66, 272, 89, 143, 370, 49, 37, 147, 121, 142, 57, 59, 116, 38, 165, 135, 107, 237, 113, 252, 87, 51, 86, 66, 330, 96, 26, 42, 20, 173, 81, 21, 65, 106, 41, 29, 123, 188, 136, 201, 148, 37, 292, 241, 144, 76, 219, 237, 74, 77, 117, 48, 58, 73, 86, 42, 131, 37, 233, 87, 121, 131, 66, 212, 197, 71, 89, 215, 38, 47, 120, 203, 62, 56, 139, 226, 34, 132, 39, 31, 86, 74, 215, 181, 127, 44, 39, 100, 79, 119, 67, 116, 46, 45, 73, 191, 40, 29, 73, 78, 136, 81, 69, 213, 127, 101, 127, 352, 130, 112, 221, 132, 133, 174, 134, 327, 167, 80, 21, 339, 47, 25, 162, 33, 134, 26, 32, 99, 34, 166, 43, 71, 79, 45, 66, 78, 89, 70, 139, 211, 111, 68, 49, 33, 29, 129, 239, 319, 74, 192, 62, 192, 73, 51, 125, 47, 29, 142, 272, 383, 198, 20, 74, 170, 257, 65, 124, 185, 145, 28, 77, 179, 43, 144, 120, 142, 34, 107, 51, 67, 24, 175, 38, 41, 205, 42, 56, 91, 51, 117, 58, 28, 87, 131, 87, 29, 184, 73, 20, 225, 33, 97, 34, 127, 28, 133, 28, 150, 169, 85, 62, 106, 35, 155, 209, 48, 56, 127, 91, 79, 56, 21, 183, 156, 75, 120, 43, 105, 110, 99, 62, 338, 92, 205, 98, 116, 128, 71, 110, 141, 194, 157, 43, 155, 92, 180, 143, 129, 54, 131, 146, 49, 172, 143, 34, 41, 83, 109, 162, 60, 23, 64, 34, 55, 30, 125, 257, 256, 147, 79, 42, 26, 207, 103, 42, 65, 110, 57, 227, 45, 130, 209, 30, 70, 123, 306, 460, 295, 95, 31, 145, 192, 138, 205, 46, 42, 266, 193, 127, 39, 94, 108, 232, 29, 63, 147, 33, 104, 106, 54, 99, 237, 433, 26, 96, 139, 154, 106, 77, 199, 49, 150, 205, 84, 78, 190, 92, 111, 25, 98, 88, 84, 45, 88, 364, 109, 78, 75, 36, 41, 19, 413, 28, 146, 76, 221, 178, 66, 145, 20, 118, 92, 211, 116, 233, 98, 192, 100, 160, 57, 87, 68, 67, 154, 171, 34, 41, 132, 97, 232, 76, 31, 63, 170, 39, 43, 166, 84, 129, 73, 22, 135, 69, 47, 166, 213, 60, 39, 320, 46, 75, 123, 166, 138, 95, 73, 40, 218, 69, 163, 38, 27, 89, 179, 75, 276, 50, 104, 112, 77, 126, 178, 28, 64, 23, 47, 54, 135, 207, 32, 76, 111, 42, 66, 22, 122, 158, 39, 142, 152, 92, 48, 114, 42, 69, 27, 67, 301, 61, 84, 206, 94, 136, 83, 70, 52, 80, 25, 23, 193, 106, 79, 141, 54, 51, 101, 78, 84, 223, 76, 119, 201, 53, 74, 118, 95, 174, 77, 60, 48, 42, 150, 347, 51, 53, 141, 84, 75, 172, 44, 129, 70, 179, 215, 61, 156, 275, 125, 299, 81, 67, 76, 21, 95, 65, 75, 57, 121, 87, 82, 104, 130, 248, 59, 236, 108, 54, 247, 106, 90, 284, 116, 125, 307, 135, 47, 320, 261, 98, 30, 50, 75, 83, 121, 55, 139, 185, 40, 156, 68, 270, 178, 32, 51, 67, 32, 82, 184, 90, 85, 171, 139, 22, 120, 202, 42, 205, 169, 40, 62, 37, 124, 103, 73, 121, 121, 84, 114, 94, 87, 44, 84, 19, 32, 169, 142, 81, 61, 75, 65, 184, 122, 102, 145, 47, 52, 62, 292, 78, 157, 34, 243, 299, 72, 43, 180, 291, 66, 103, 111, 74, 158, 40, 76, 139, 91, 27, 244, 57, 215, 169, 133, 78, 113, 236, 144, 146, 191, 38, 154, 42, 42, 143, 422, 180, 102, 50, 316, 108, 96, 182, 275, 49, 101, 56, 38, 191, 72, 88, 63, 44, 221, 399, 85, 21, 44, 142, 92, 180, 60, 116, 133, 214, 42, 23, 61, 213, 205, 61, 28, 145, 67, 113, 29, 124, 42, 64, 75, 264, 145, 182, 224, 208, 126, 36, 35, 48, 358, 88, 176, 58, 51, 45, 102, 96, 18, 264, 64, 32, 38, 51, 79, 127, 68, 22, 132, 169, 77, 94, 297, 68, 117, 80, 161, 176, 30, 165, 216, 37, 130, 27, 45, 130, 104, 63, 59, 58, 49, 229, 88, 171, 46, 85, 102, 153, 46, 39, 131, 31, 128, 86, 198, 66, 199, 126, 96, 101, 40, 142, 52, 91, 70, 59, 191, 23, 83, 225, 97, 51, 186, 122, 162, 66, 335, 49, 254, 29, 50, 402, 81, 93, 187, 264, 240, 202, 116, 505, 78, 47, 49, 125, 113, 61, 30, 104, 81, 224, 74, 141, 45, 191, 54, 67, 111, 151, 180, 43, 33, 65, 100, 258, 41, 27, 148, 217, 156, 82, 98, 150, 19, 49, 97, 71, 86, 159, 29, 58, 39, 46, 68, 65, 144, 153, 64, 130, 49, 105, 31, 41, 224, 37, 168, 35, 83, 157, 29, 175, 54, 144, 85, 145, 28, 93, 130, 40, 58, 344, 151, 80, 65, 411, 53, 92, 78, 457, 101, 165, 91, 109, 188, 76, 55, 75, 42, 50, 78, 114, 84, 48, 218, 47, 44, 58, 130, 131, 148, 68, 74, 150, 305, 254, 102, 32, 150, 171, 87, 57, 140, 86, 157, 111, 126, 114, 297, 136, 431, 36, 57, 81, 79, 37, 178, 271, 182, 56, 93, 69, 132, 57, 159, 138, 54, 93, 224, 93, 111, 79, 18, 125, 156, 251, 98, 93, 24, 44, 174, 141, 107, 187, 41, 100, 59, 95, 40, 77, 181, 119, 77, 34, 175, 41, 321, 67, 20, 250, 127, 153, 112, 47, 170, 116, 97, 177, 58, 57, 46, 109, 29, 110, 38, 86, 172, 132, 28, 187, 67, 45, 280, 91, 49, 153, 138, 63, 66, 78, 219, 120, 127, 30, 128, 28, 74, 77, 426, 21, 26, 117, 139, 45, 38, 55, 152, 104, 128, 29, 22, 28, 73, 47, 149, 94, 104, 104, 76, 33, 74, 38, 387, 31, 208, 38, 266, 116, 482, 194, 193, 103, 134, 46, 20, 114, 89, 47, 62, 219, 34, 25, 98, 65, 42, 38, 79, 171, 80, 34, 184, 43, 93, 78, 74, 33, 53, 196, 116, 76, 91, 41, 65, 117, 57, 41, 31, 52, 43, 83, 281, 51, 78, 77, 105, 57, 164, 280, 116, 48, 165, 120, 215, 239, 102, 78, 113, 52, 161, 39, 181, 177, 138, 31, 99, 311, 14, 44, 33, 56, 288, 75, 136, 86, 188, 139, 326, 74, 380, 45, 134, 135, 15, 73, 171, 78, 80, 48, 82, 44, 71, 213, 75, 524, 56, 49, 80, 64, 135, 201, 210, 24, 53, 205, 64, 167, 89, 211, 29, 73, 78, 92, 83, 47, 130, 138, 25, 106, 50, 132, 45, 68, 117, 224, 45, 66, 65, 141, 42, 44, 153, 70, 59, 233, 99, 33, 155, 184, 35, 31, 370, 91, 155, 171, 98, 88, 63, 31, 128, 33, 34, 51, 284, 202, 41, 51, 38, 108, 80, 530, 112, 180, 78, 56, 103, 250, 134, 29, 212, 46, 233, 44, 62, 58, 88, 83, 93, 90, 166, 202, 88, 185, 108, 53, 110, 74, 150, 160, 54, 159, 117, 95, 85, 131, 165, 46, 92, 174, 32, 36, 397, 65, 64, 59, 303, 47, 19, 177, 42, 232, 101, 68, 81, 264, 112, 23, 159, 124, 122, 51, 151, 46, 250, 71, 29, 50, 70, 57, 73, 133, 70, 180, 118, 170, 165, 34, 203, 141, 23, 150, 43, 110, 23, 25, 112, 139, 36, 147, 86, 151, 127, 149, 282, 69, 115, 55, 52, 222, 144, 353, 199, 60, 49, 103, 56, 80, 34, 44, 112, 82, 72, 69, 61, 41, 64, 194, 71, 51, 38, 158, 109, 52, 94, 75, 38, 196, 107, 52, 27, 160, 172, 87, 262, 132, 38, 204, 18, 93, 141, 106, 85, 131, 82, 128, 23, 66, 128, 176, 142, 51, 120, 76, 29, 126, 77, 64, 68, 127, 221, 100, 124, 44, 33, 204, 90, 132, 76, 84, 51, 17, 37, 46, 198, 135, 545, 104, 45, 188, 295, 110, 204, 138, 131, 225, 60, 147, 48, 218, 156, 54, 107, 41, 235, 120, 81, 47, 39, 139, 34, 74, 39, 52, 64, 54, 204, 169, 214, 67, 43, 184, 107, 126, 266, 47, 61, 60, 34, 47, 34, 105, 115, 177, 112, 103, 81, 236, 102, 122, 149, 163, 43, 92, 176, 91, 90, 297, 29, 343, 38, 71, 91, 71, 176, 35, 115, 36, 77, 49, 119, 122, 49, 49, 71, 60, 186, 33, 49, 99, 142, 135, 40, 53, 324, 156, 78, 60, 175, 145, 114, 63, 42, 218, 87, 31, 167, 83, 85, 78, 93, 64, 68, 77, 22, 119, 116, 160, 144, 26, 59, 202, 213, 26, 92, 61, 126, 24, 80, 237, 121, 138, 85, 222, 71, 13, 86, 68, 119, 100, 116, 46, 197, 86, 23, 185, 51, 27, 93, 91, 143, 36, 247, 262, 88, 88, 34, 25, 60, 24, 357, 44, 235, 131, 82, 48, 56, 271, 96, 132, 90, 128, 38, 83, 101, 79, 109, 33, 137, 90, 182, 73, 55, 131, 49, 133, 140, 185, 33, 163, 42, 53, 32, 167, 239, 69, 53, 68, 63, 194, 56, 245, 240, 38, 410, 164, 113, 50, 142, 291, 65, 204, 57, 154, 44, 89, 33, 256, 114, 216, 15, 138, 50, 174, 184, 106, 159, 97, 22, 304, 81, 52, 169, 64, 131, 57, 42, 204, 101, 46, 131, 39, 46, 101, 84, 104, 58, 109, 66, 87, 141, 60, 106, 96, 130, 166, 208, 286, 72, 143, 139, 231, 45, 94, 42, 224, 83, 49, 65, 65, 111, 298, 61, 154, 42, 73, 134, 78, 71, 112, 62, 28, 43, 25, 69, 63, 119, 89, 131, 56, 39, 178, 93, 130, 222, 216, 283, 170, 114, 118, 37, 44, 214, 105, 73, 67, 64, 94, 49, 87, 34, 263, 85, 64, 34, 83, 31, 57, 86, 225, 34, 90, 60, 90, 38, 93, 286, 111, 69, 41, 72, 89, 107, 44, 141, 24, 51, 22, 126, 72, 225, 71, 146, 103, 245, 210, 32, 20, 99, 41, 107, 93, 160, 350, 84, 75, 124, 145, 149, 229, 34, 87, 129, 75, 118, 39, 32, 36, 163, 143, 39, 90, 78, 46, 59, 83, 50, 113, 247, 111, 67, 55, 120, 97, 79, 380, 207, 94, 59, 203, 27, 367, 190, 96, 105, 101, 60, 27, 85, 37, 26, 84, 133, 111, 110, 30, 48, 45, 44, 113, 197, 157, 106, 129, 62, 164, 57, 45, 63, 67, 44, 44, 77, 88, 103, 67, 33, 165, 48, 27, 41, 96, 82, 128, 51, 124, 58, 52, 84, 155, 90, 91, 162, 96, 71, 121, 90, 103, 227, 24, 82, 37, 190, 192, 51, 33, 238, 153, 132, 34, 372, 164, 101, 151, 248, 35, 51, 114, 204, 69, 138, 95, 157, 196, 262, 105, 82, 42, 49, 146, 197, 30, 67, 168, 119, 86, 170, 62, 141, 131, 92, 83, 168, 96, 33, 81, 103, 72, 100, 41, 43, 54, 49, 36, 44, 96, 64, 246, 56, 96, 352, 101, 31, 92, 88, 104, 114, 25, 117, 80, 192, 137, 98, 48, 118, 57, 24, 37, 142, 85, 142, 80, 193, 45, 56, 74, 136, 47, 135, 83, 56, 69, 145, 38, 49, 206, 62, 30, 106, 128, 100, 361, 38, 127, 67, 87, 47, 85, 136, 33, 44, 290, 167, 58, 49, 89, 73, 91, 25, 72, 47, 103, 294, 53, 62, 51, 124, 34, 350, 73, 100, 78, 90, 36, 68, 241, 132, 87, 63, 68, 151, 86, 57, 184, 42, 53, 115, 49, 22, 170, 66, 100, 48, 123, 200, 92, 76, 180, 130, 126, 244, 66, 147, 240, 79, 305, 89, 212, 165, 54, 46, 261, 145, 29, 111, 30, 119, 127, 100, 70, 32, 123, 52, 90, 399, 182, 58, 66, 124, 43, 33, 76, 28, 98, 156, 194, 82, 77, 257, 119, 58, 160, 382, 122, 127, 56, 129, 60, 100, 254, 36, 114, 164, 70, 107, 128, 123, 163, 55, 65, 291, 39, 109, 119, 224, 26, 73, 84, 45, 65, 75, 90, 44, 72, 52, 72, 56, 140, 56, 89, 63, 61, 40, 37, 194, 250, 543, 92, 46, 51, 88, 63, 85, 63, 59, 108, 79, 150, 51, 178, 139, 261, 61, 85, 119, 97, 153, 197, 51, 181, 99, 74, 174, 116, 98, 35, 134, 129, 143, 93, 77, 202, 220, 26, 231, 58, 143, 167, 156, 89, 53, 105, 60, 115, 84, 29, 32, 49, 40, 162, 54, 35, 61, 49, 71, 125, 21, 67, 48, 63, 78, 93, 312, 265, 110, 52, 106, 215, 62, 157, 104, 134, 102, 67, 73, 52, 61, 257, 40, 37, 227, 110, 34, 109, 179, 137, 95, 32, 50, 20, 146, 41, 105, 89, 100, 67, 123, 45, 86, 27, 111, 57, 64, 65, 94, 83, 62, 58, 93, 180, 31, 96, 99, 80, 21, 27, 96, 29, 96, 37, 160, 66, 83, 62, 376, 129, 382, 296, 122, 213, 36, 28, 95, 507, 50, 118, 60, 164, 263, 55, 80, 17, 100, 52, 18, 50, 26, 40, 150, 76, 45, 131, 72, 243, 93, 91, 72, 117, 69, 130, 93, 36, 99, 62, 53, 53, 126, 129, 13, 308, 38, 56, 103, 159, 129, 39, 139, 49, 152, 88, 91, 61, 134, 34, 112, 140, 62, 47, 75, 163, 106, 75, 149, 210, 52, 102, 25, 81, 58, 73, 62, 151, 67, 170, 85, 158, 60, 24, 112, 143, 190, 36, 113, 85, 49, 23, 181, 91, 52, 145, 41, 74, 43, 40, 44, 67, 179, 119, 141, 114, 97, 187, 108, 45, 59, 164, 96, 173, 66, 50, 243, 147, 92, 98, 77, 117, 54, 42, 67, 177, 67, 25, 209, 46, 86, 243, 96, 41, 212, 28, 143, 121, 218, 123, 27, 117, 231, 71, 73, 80, 77, 174, 47, 54, 157, 78, 41, 57, 48, 88, 205, 170, 28, 234, 169, 60, 72, 127, 47, 143, 245, 244, 160, 68, 23, 33, 47, 79, 42, 57, 52, 190, 64, 73, 235, 174, 73, 55, 52, 36, 132, 92, 84, 63, 127, 85, 36, 65, 96, 86, 61, 198, 88, 83, 95, 103, 112, 112, 57, 126, 95, 42, 93, 35, 87, 187, 62, 18, 110, 14, 80, 156, 46, 64, 86, 43, 79, 389, 44, 173, 117, 99, 78, 75, 37, 160, 71, 47, 58, 51, 175, 91, 151, 123, 324, 27, 47, 56, 84, 111, 66, 49, 134, 94, 233, 113, 59, 29, 351, 265, 58, 132, 192, 196, 130, 127, 35, 54, 61, 133, 158, 73, 36, 69, 250, 47, 105, 66, 57, 371, 229, 79, 86, 155, 117, 53, 38, 102, 71, 175, 26, 139, 38, 90, 115, 102, 70, 52, 242, 139, 39, 100, 74, 176, 111, 121, 99, 56, 267, 139, 169, 29, 86, 203, 142, 27, 116, 133, 36, 47, 73, 86, 240, 99, 148, 148, 218, 169, 79, 97, 178, 172, 55, 190, 106, 89, 310, 117, 87, 57, 169, 289, 61, 260, 23, 39, 89, 32, 41, 525, 183, 78, 24, 135, 91, 136, 129, 34, 338, 55, 33, 155, 104, 26, 109, 43, 89, 89, 90, 24, 49, 54, 106, 44, 146, 62, 35, 151, 26, 78, 202, 90, 63, 82, 45, 141, 262, 56, 259, 149, 120, 171, 114, 120, 30, 36, 48, 87, 42, 59, 84, 16, 42, 40, 37, 226, 147, 37, 68, 76, 29, 163, 141, 82, 68, 57, 37, 71, 84, 97, 66, 47, 100, 59, 215, 19, 65, 47, 133, 96, 89, 79, 190, 22, 384, 62, 78, 34, 148, 81, 73, 217, 164, 73, 123, 49, 151, 34, 175, 83, 118, 17, 178, 154, 227, 156, 93, 545, 163, 45, 27, 87, 141, 54, 104, 50, 56, 23, 56, 82, 83, 69, 69, 84, 51, 78, 221, 143, 92, 82, 51, 121, 48, 37, 194, 35, 46, 181, 68, 86, 76, 71, 103, 76, 90, 37, 74, 157, 259, 211, 94, 119, 32, 105, 43, 137, 56, 102, 44, 124, 26, 107, 142, 39, 80, 83, 75, 173, 105, 26, 73, 32, 28, 42, 180, 150, 63, 85, 158, 66, 100, 157, 92, 42, 108, 59, 90, 74, 44, 52, 50, 60, 149, 79, 53, 203, 83, 71, 348, 103, 67, 38, 198, 96, 85, 54, 408, 109, 35, 80, 92, 342, 73, 59, 41, 116, 85, 25, 98, 69, 62, 57, 126, 193, 121, 56, 50, 188, 113, 192, 130, 59, 135, 97, 85, 33, 254, 117, 72, 192, 75, 235, 32, 89, 131, 77, 54, 259, 36, 60, 271, 29, 89, 47, 31, 91, 26, 34, 108, 22, 117, 57, 62, 100, 75, 58, 36, 22, 110, 114, 38, 29, 97, 74, 104, 57, 35, 123, 336, 65, 119, 93, 144, 40, 74, 22, 66, 437, 27, 184, 92, 330, 325, 107, 41, 306, 114, 108, 216, 173, 496, 42, 39, 44, 314, 82, 60, 112, 46, 279, 76, 73, 39, 213, 25, 57, 180, 80, 137, 138, 41, 45, 44, 166, 228, 88, 55, 144, 86, 49, 43, 175, 164, 59, 134, 113, 63, 37, 160, 125, 69, 130, 156, 47, 160, 194, 120, 63, 105, 405, 21, 161, 32, 31, 190, 107, 51, 99, 107, 122, 60, 100, 169, 386, 96, 145, 68, 84, 75, 140, 89, 146, 103, 225, 123, 18, 124, 138, 241, 221, 329, 84, 195, 62, 117, 75, 129, 157, 32, 272, 52, 106, 30, 47, 135, 119, 413, 253, 167, 263, 59, 84, 49, 115, 63, 87, 142, 372, 73, 77, 60, 154, 46, 52, 42, 243, 171, 44, 94, 23, 72, 29, 146, 154, 142, 180, 39, 133, 105, 31, 80, 81, 63, 55, 73, 35, 78, 100, 48, 34, 78, 65, 125, 52, 147, 50, 120, 39, 80, 249, 138, 127, 86, 44, 92, 75, 100, 32, 116, 84, 45, 63, 168, 202, 299, 162, 87, 50, 93, 201, 29, 33, 181, 89, 64, 128, 76, 203, 64, 86, 122, 61, 147, 223, 38, 86, 93, 180, 165, 53, 36, 85, 115, 120, 67, 26, 79, 168, 115, 34, 122, 295, 182, 73, 73, 155, 156, 39, 102, 104, 122, 72, 146, 85, 193, 366, 207, 218, 76, 43, 59, 101, 38, 72, 86, 63, 144, 223, 30, 31, 287, 82, 98, 134, 432, 224, 129, 162, 81, 162, 55, 104, 67, 103, 116, 86, 31, 66, 90, 95, 26, 97, 46, 131, 60, 38, 69, 77, 97, 187, 47, 318, 42, 140, 106, 114, 77, 125, 35, 89, 44, 130, 36, 139, 112, 252, 42, 16, 133, 174, 78, 191, 79, 69, 40, 35, 113, 23, 54, 23, 123, 168, 48, 106, 60, 241, 159, 154, 221, 90, 103, 69, 43, 71, 85, 53, 254, 27, 42, 119, 68, 67, 45, 51, 67, 91, 38, 74, 73, 42, 32, 160, 260, 50, 104, 81, 36, 80, 111, 32, 35, 34, 74, 67, 24, 76, 51, 36, 67, 37, 99, 76, 108, 83, 252, 43, 62, 110, 167, 32, 184, 53, 368, 60, 168, 90, 82, 115, 20, 49, 73, 132, 62, 185, 112, 153, 81, 25, 122, 83, 59, 79, 223, 39, 119, 48, 66, 70, 126, 71, 189, 117, 53, 309, 203, 33, 51, 82, 68, 99, 126, 54, 63, 132, 191, 57, 139, 75, 372, 30, 114, 139, 11, 280, 41, 165, 98, 109, 149, 219, 70, 136, 51, 163, 135, 51, 32, 58, 172, 48, 111, 83, 56, 49, 36, 108, 111, 138, 68, 177, 120, 164, 160, 69, 180, 248, 91, 213, 71, 35, 49, 41, 43, 44, 348, 165, 125, 85, 25, 90, 132, 45, 128, 57, 73, 31, 44, 38, 52, 28, 75, 36, 53, 65, 148, 95, 129, 117, 159, 92, 41, 235, 48, 77, 147, 50, 82, 177, 67, 201, 127, 102, 73, 80, 74, 159, 194, 63, 69, 123, 114, 69, 108, 62, 92, 49, 80, 29, 132, 233, 36, 91, 162, 78, 60, 138, 232, 102, 102, 83, 124, 77, 132, 183, 177, 38, 91, 95, 104, 307, 25, 52, 140, 117, 126, 186, 111, 86, 186, 83, 60, 126, 49, 90, 98, 67, 145, 69, 78, 89, 180, 44, 36, 214, 260, 175, 61, 142, 21, 53, 59, 136, 82, 69, 24, 218, 219, 207, 61, 41, 165, 105, 111, 100, 82, 138, 63, 216, 210, 82, 106, 107, 141, 276, 113, 94, 249, 29, 43, 106, 98, 91, 196, 76, 112, 121, 31, 90, 73, 78, 35, 35, 45, 97, 28, 47, 264, 78, 43, 51, 28, 23, 83, 18, 40, 26, 87, 81, 46, 166, 261, 234, 155, 114, 17, 81]
print(len(x))
print(sum(x) / len(x))
plt.figure(figsize=(10, 5))
plt.hist(x, 30)
plt.show()