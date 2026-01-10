from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as ReportLabImage, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
from datetime import datetime
from PIL import Image
import os

class ReportGenerator:
    """
    Service for generating PDF reports for disease detection results.
    """
    
    @staticmethod
    def generate_pdf_report(prediction_result, disease_info, crop_type, uploaded_image=None):
        """
        Generates a PDF report using ReportLab.
        
        Args:
            prediction_result: The result object from the prediction handler.
            disease_info (dict): Dictionary containing details about the disease.
            crop_type (str): Type of crop (e.g., "Rice", "Pulse").
            uploaded_image (PIL.Image): The image uploaded by the user.
            
        Returns:
            bytes: The generated PDF content.
        """
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
        
        styles = getSampleStyleSheet()
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1e3a8a'),
            alignment=1, # Center
            spaceAfter=30
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#2563eb'),
            spaceBefore=15,
            spaceAfter=10
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=11,
            leading=14
        )
        
        story = []
        
        # 1. Title
        story.append(Paragraph("Agricultural Disease Analysis Report", title_style))
        story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 
                             ParagraphStyle('Date', parent=body_style, alignment=1)))
        story.append(Spacer(1, 20))
        
        # 2. Image (if available)
        if uploaded_image:
            try:
                # Save PIL image to bytes to use in ReportLab
                img_io = BytesIO()
                # Ensure image is RGB
                if uploaded_image.mode != 'RGB':
                    uploaded_image = uploaded_image.convert('RGB')
                    
                # Resize for report if too large, keeping aspect ratio
                max_width = 4 * inch
                max_height = 3 * inch
                img_width, img_height = uploaded_image.size
                ratio = min(max_width/img_width, max_height/img_height)
                new_size = (int(img_width * ratio), int(img_height * ratio))
                
                # We don't necessarily need to resize the actual bits, ReportLab can scale,
                # but let's be safe with memory
                
                uploaded_image.save(img_io, format='JPEG', quality=85)
                img_io.seek(0)
                
                rl_image = ReportLabImage(img_io, width=new_size[0], height=new_size[1])
                story.append(rl_image)
                story.append(Spacer(1, 20))
            except Exception as e:
                story.append(Paragraph(f"[Process Image Error: {str(e)}]", body_style))
        
        # 3. Diagnosis Summary Table
        data = [
            ["Analysis Parameter", "Result"],
            ["Crop Type", crop_type.replace("🌾 ", "").replace("🫘 ", "")],
            ["Detected Condition", prediction_result.predicted_class],
            ["Confidence Score", f"{prediction_result.confidence_score:.1f}%"],
            ["Severity", disease_info.get('severity', 'Unknown')]
        ]
        
        table = Table(data, colWidths=[2.5*inch, 3*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (1, 0), colors.HexColor('#3b82f6')),
            ('TEXTCOLOR', (0, 0), (1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0f9ff')),
            ('GRID', (0, 0), (-1, -1), 1, colors.white),
            ('PADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(table)
        story.append(Spacer(1, 20))
        
        # 4. Detailed Information
        story.append(Paragraph("Disease Details", heading_style))
        
        # Overview
        story.append(Paragraph("<b>Overview:</b>", body_style))
        overview_text = disease_info.get('overview', disease_info.get('description', 'N/A'))
        story.append(Paragraph(overview_text, body_style))
        story.append(Spacer(1, 10))

        # Symptoms
        story.append(Paragraph("<b>Symptoms:</b>", body_style))
        story.append(Paragraph(disease_info.get('symptoms', 'N/A'), body_style))
        story.append(Spacer(1, 10))
        
        # Quick Treatment
        story.append(Paragraph("<b>Quick Treatment:</b>", body_style))
        story.append(Paragraph(disease_info.get('treatment', 'N/A'), body_style))
        story.append(Spacer(1, 15))

        # 5. Prevention Tips
        prevention_tips = disease_info.get('prevention', [])
        if prevention_tips:
            story.append(Paragraph("Prevention Tips", heading_style))
            list_items = [ListItem(Paragraph(tip, body_style)) for tip in prevention_tips]
            t_list = ListFlowable(
                list_items,
                bulletType='bullet',
                start='circle',
                leftIndent=20,
                spaceAfter=10
            )
            story.append(t_list)
            story.append(Spacer(1, 15))
            
        # 6. Practical Treatment Guidance
        treatment_steps = disease_info.get('treatment_guidance', disease_info.get('cure_steps', []))
        if treatment_steps:
            story.append(Paragraph("Practical Treatment Guidance", heading_style))
            list_items = [ListItem(Paragraph(step, body_style)) for step in treatment_steps]
            t_list = ListFlowable(
                list_items,
                bulletType='bullet',
                start='circle',
                leftIndent=20,
                spaceAfter=10
            )
            story.append(t_list)
            story.append(Spacer(1, 20))

        story.append(Spacer(1, 30))
        
        # 5. Disclaimer
        disclaimer_style = ParagraphStyle(
            'Disclaimer',
            parent=body_style,
            fontSize=8,
            textColor=colors.gray,
            alignment=1 # Center
        )
        story.append(Paragraph(" "
                               "", 
                               disclaimer_style))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
