export interface FieldProps {
  label?: string;
  placeholder?: string;
  value?: string;
  onChange?: (value: string) => void;
  invalid?: boolean;
  /** Shown under the field when invalid — the colour never carries the state alone. */
  message?: string;
  className?: string;
}

export function Field({
  label,
  placeholder,
  value,
  onChange,
  invalid = false,
  message,
  className,
}: FieldProps) {
  return (
    <label className={['td-field', className].filter(Boolean).join(' ')}>
      {label !== undefined && <span className="td-field__label">{label}</span>}
      <input
        className={['td-field__input', invalid ? 'td-field__input--invalid' : undefined]
          .filter(Boolean)
          .join(' ')}
        placeholder={placeholder}
        value={value}
        aria-invalid={invalid || undefined}
        onChange={(e) => onChange?.(e.target.value)}
      />
      {invalid && message !== undefined && (
        <span className="td-field__message">{message}</span>
      )}
    </label>
  );
}
