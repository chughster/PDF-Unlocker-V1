import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pikepdf


def remove_pdf_password():
    # Create a root window but hide it
    root = tk.Tk()
    root.withdraw()

    # Open file selection dialog
    input_path = filedialog.askopenfilename(
        title="Select PDF file to unlock",
        filetypes=[("PDF files", "*.pdf")]
    )

    # Check if a file was selected
    if not input_path:
        messagebox.showinfo("Cancelled", "No file selected.")
        return

    # Generate output path
    directory = os.path.dirname(input_path)
    filename = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(directory, f"{filename}_unlocked.pdf")

    try:
        # Attempt to open the PDF
        pdf = pikepdf.Pdf.open(input_path)

        # Save the unlocked PDF
        pdf.save(output_path)

        # Close the PDF
        pdf.close()

        # Show success message
        messagebox.showinfo(
            "Success",
            f"PDF successfully unlocked!\nNew file created at:\n{output_path}"
        )

    except pikepdf.PasswordError:
        # Prompt for password if the PDF is encrypted
        password = tk.simpledialog.askstring(
            "Password Required",
            "Enter PDF password:",
            show='*'
        )

        if password:
            try:
                # Try to open PDF with provided password
                pdf = pikepdf.Pdf.open(input_path, password=password)

                # Save the unlocked PDF
                pdf.save(output_path)

                # Close the PDF
                pdf.close()

                # Show success message
                messagebox.showinfo(
                    "Success",
                    f"PDF successfully unlocked!\nNew file created at:\n{output_path}"
                )

            except pikepdf.PasswordError:
                messagebox.showerror("Error", "Incorrect password.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showinfo("Cancelled", "Password entry cancelled.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Ensure the script runs the main function when executed
if __name__ == "__main__":
    remove_pdf_password()