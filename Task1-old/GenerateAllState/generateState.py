import itertools
import pickle
import os

def generate_all_states(file_path):
    """
    Generate all possible 8-puzzle states (9! states) and save them to a file.
    
    Mỗi state được biểu diễn dưới dạng bảng 3x3: danh sách các list có 3 phần tử.
    Sử dụng itertools.permutations để tạo ra tất cả các permutation của các số từ 0 đến 8.
    """
    all_states = []
    
    # Duyệt qua tất cả các permutation của các số từ 0 đến 8 (9! = 362880 trạng thái)
    for perm in itertools.permutations(range(9)):
        # Chia flat tuple perm thành 3 hàng, mỗi hàng 3 số
        board = [list(perm[i:i+3]) for i in range(0, 9, 3)]
        all_states.append(board)
    
    # Đảm bảo thư mục để lưu file tồn tại
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Lưu list các trạng thái vào file sử dụng pickle
    with open(file_path, 'wb') as f:
        pickle.dump(all_states, f)
    
    print(f"Đã lưu {len(all_states)} trạng thái vào file: {file_path}")

# Chạy hàm generate_all_states để tạo và lưu toàn bộ trạng thái của 8-puzzle
generate_all_states('./all_states_8_puzzles.pkl')



# def load_all_states(file_path):
#     with open(file_path, 'rb') as f:
#         states = pickle.load(f)
#     return states

# # Kiểm tra: Load lại các trạng thái đã lưu và in ra số lượng cũng như 5 trạng thái đầu tiên
# loaded_states = load_all_states('./Task1/GenerateAllState/all_states_8_puzzles.pkl')
# print("Số trạng thái đã load:", len(loaded_states))
# for i in range(5):
#     print(f"Trạng thái thứ {i+1}:")
#     for row in loaded_states[i]:
#         print(row)
#     print()
