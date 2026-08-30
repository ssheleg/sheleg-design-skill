export interface FieldProps {
  label: string;
  placeholder?: string;
  value?: string;
  onChange?: (next: string) => void;
  /** The filled control seated inside the field's right edge. */
  action?: string;
  onAction?: () => void;
  className?: string;
}

export function Field({
  label,
  placeholder,
  value,
  onChange,
  action,
  onAction,
  className,
}: FieldProps) {
  return (
    <label className={['ch-field', className].filter(Boolean).join(' ')}>
      <span className="ch-field__label">{label}</span>
      <span className="ch-field__box">
        <input
          className="ch-field__input"
          type="text"
          placeholder={placeholder}
          value={value}
          onChange={(e) => onChange?.(e.target.value)}
        />
        {action && (
          <button type="button" className="ch-field__action" onClick={onAction}>
            {action}
          </button>
        )}
      </span>
    </label>
  );
}
